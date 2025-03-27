import requests

class PDFReader:
    def __init__(self, url):
        self.url = url
        self.pdf_data = None
        self.pdf_reader = None
        self.page_number = None
    def download_pdf(self):
        try:
            # Send a GET request to the URL
            response = requests.get(self.url)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Open a file to write the PDF content
                with open("downloaded_file.pdf", "wb") as file:
                    file.write(response.content)
                print("PDF downloaded successfully!")
            else:
                print(f"Failed to download PDF. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
    def get_num_pages(self):
        pass

url = 'https://pdfobject.com/pdf/sample.pdf'
pdf = PDFReader(url = url)
pdf.download_pdf()