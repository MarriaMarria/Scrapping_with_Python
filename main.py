import requests
import pprint
from bs4 import BeautifulSoup

# This code performs an HTTP request to the given URL. It retrieves the 
# HTML data that the server sends back and stores that data in a Python object.


URL = 'https://fr.indeed.com/jobs?q=Developpeur+Cloud&l=Paris+%2875%29'
page = requests.get(URL)

# soup = BeautifulSoup(page.content, 'html.parser')
soup = BeautifulSoup(page.content, 'lxml')

# taking the div with all results
results = soup.find(id='resultsCol')


# jobtitle is a class which is associated to open positions
# jobtitle = results.findAll('a', {'class' : 'jobtitle'})
# for title in jobtitle:
    # print(title.prettify())
    # print('_______________')
    # prints the <a> elements with the class jobtitle

# finds job titles 15
# job_result = soup.findAll('a', {'class': 'jobtitle'})
# for job in job_result:
#     title = job.get('title')
#     print(title)
#     print('_______________')

# finds when annonce posted
# date_result = soup.findAll('span', {'class': 'date'})
# for date in date_result:
#     print(date.text)
# print(date_result)

# jobtitle2 = soup.findAll('a', {'class': 'turnstileLink'},)
# for job in jobtitle2:
#     print(job.text) # I tried to see companies as they are in <a> tag's text field...But I get againg the job positions

# gives me 15 locations
locations = results.find_all(['div', 'span'], {'class' : 'location'})
for location in locations:
    print(location.text)

