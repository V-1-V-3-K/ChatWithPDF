import os
import requests
import fitz

class PDFReader:
    def __init__(self, url):
        self.url = url
        self.pdf_data = []
        self.pdf_reader = None
        self.page_number = None
        
        # Get the absolute path of the "Backend/pdfs" directory
        backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Moves up to "Backend"
        self.pdf_dir = os.path.join(backend_dir, "pdfs")  # Target "pdfs" inside "Backend"
        self.pdf_path = os.path.join(self.pdf_dir, "downloaded_file.pdf")
        os.makedirs(self.pdf_dir, exist_ok=True)

    def download_pdf(self):
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(self.pdf_path), exist_ok=True)

            # Send a GET request to the URL with timeout to avoid hanging requests
            response = requests.get(self.url, timeout=10)
            # Raises HTTPError for 4xx or 5xx responses
            response.raise_for_status()
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Save the PDF file
                
                with open(self.pdf_path, "wb") as file:
                    file.write(response.content)
                print("PDF downloaded successfully!")

                ## call internal function to process data
                self.__process_pdf()
                
            else:
                raise Exception(f"Failed to download PDF. Status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred: {e}")
    
    def __process_pdf(self):
        try:
            ## open file
            doc = fitz.open(self.pdf_path)
            
            ## get total page number
            self.page_number = len(doc)

            ## fetch page data from each page and save it
            for page_num in range(self.page_number):
                page = doc[page_num]
                text = page.get_text("text")
                self.pdf_data.append(text)

            ## close file
            doc.close()
        except Exception as e:
            raise Exception(f"Error processing PDF: {e}")

    def get_num_pages(self):
        return self.page_number
    
    def get_page_data(self,pageNumber):
        try:
            if not (1 <= pageNumber <= self.page_number):
                print(f"❌ Invalid page number: {pageNumber}. Must be between 1 and {self.page_number}.")
                return None  # Graceful handling

            return self.pdf_data[pageNumber-1] 
            
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def get_pdf_data(self):
        """Yield PDF data page by page to optimize memory usage."""
        for page in self.pdf_data:
            yield page  # Returns pages one at a time instead of storing everything



## test code
## uncomment the below lines and run python .\url.py to check if code is working properly
# url = 'https://pdfobject.com/pdf/sample.pdf'
# pdf = PDFReader(url = url)
# pdf.download_pdf()
# print(pdf.get_num_pages())
# print(pdf.get_page_data(1))
# for page_content in pdf.get_pdf_data():
    # print(page_content) 
# pdf.get_page_data(2)

