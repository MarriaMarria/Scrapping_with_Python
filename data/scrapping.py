import requests
from bs4 import BeautifulSoup
import sqlite3


class Scrapping():

    def __init__(self):
        self.url = "https://fr.indeed.com/emplois?q=developpeur+web&l=Paris+%2875%29"
        self.href_list = None
        self.title_list = None
        self.locations_list = None
        self.date_lists = None

    def read_and_soup(self):
        page = requests.get(self, url)
        soup = BeautifulSoup(page.content, 'lxml')
        results = soup.find(id='resultsCol')
        a_links = results.find_all('a', class_ = 'jobtitle turnstileLink')
    
    def loop_links(self)