import requests
import pprint
from bs4 import BeautifulSoup

# This code performs an HTTP request to the given URL. It retrieves the 
# HTML data that the server sends back and stores that data in a Python object.


URL = 'https://fr.indeed.com/jobs?q=Developpeur+Cloud&l=Paris+%2875%29'
page = requests.get(URL)
# pprint.pprint(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# find elements by ID
results = soup.find(id='resultsCol')
# print(results.prettify())

# find elements by class
date_published = results.find_all('div', class_='date')
print(results.prettify())
# print(date_published)

jobtitle = results.find(class_ = 'jobtitle turnstileLink visited')
print(jobtitle.prettify())