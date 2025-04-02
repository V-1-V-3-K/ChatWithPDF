import requests
import os
from bs4 import BeautifulSoup

class RepoPdfReader:
    def __init__(self,repo_url):
        self.repo_url = repo_url
        self.pdf_links = []
        self.pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","pdfs"))
        # Ensure the directory exists 
        os.makedirs(self.pdf_path, exist_ok=True)


    def download_pdf(self):
        """
        Scrape the webpage to get all PDF links.
        """

        try:
            response = requests.get(self.repo_url, timeout=10) 
            response.raise_for_status()

            # Parse the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <a> tags with href attribute that ends with '.pdf'
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if href.lower().endswith('.pdf'):
                    self.pdf_links.append(href)
            
            self.__download_all_pdf()

        except Exception as e:
            print(f"Error while scraping: {e}")

    
    def __download_all_pdf(self):
        
        if self.pdf_links == []:
            raise Exception('No Pdf Links Found')
        pass