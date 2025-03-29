import requests
import fitz

class PDFReader:
    def __init__(self, url):
        self.url = url
        self.pdf_data = []
        self.pdf_reader = None
        self.page_number = None
        self.pdf_path = None
    def download_pdf(self):
        try:
            # Send a GET request to the URL
            response = requests.get(self.url)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Save the PDF file
                self.pdf_path = "downloaded_file.pdf"
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
            raise Exception(e)

    def get_num_pages(self):
        return self.page_number
    
    def get_page_data(self,pageNumber):
        try:
            if(pageNumber>self.page_number):
                raise Exception(f'Page number provided:{pageNumber} is should be strictly less than size of pdf:{self.page_number}')
            
            if(pageNumber<1):
                raise Exception(f'Page number provided:{pageNumber} should be strictly greater than 0')

            return self.pdf_data[pageNumber-1] 
            
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def get_pdf_data(self):
        ## return full pdf data
        return self.pdf_data



## test code
## uncomment the below lines and run python .\url.py to check if code is working properly
# url = 'https://pdfobject.com/pdf/sample.pdf'
# pdf = PDFReader(url = url)
# pdf.download_pdf()
# print(pdf.get_num_pages())
# print(pdf.get_page_data(1))
# print(pdf.get_pdf_data())
# pdf.get_page_data(2)

