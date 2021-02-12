import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://fr.indeed.com/emplois?q=developpeur+web&l=Paris+%2875%29'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')

# taking the div with all results
results = soup.find(id='resultsCol')
a_links = results.find_all('a', class_ = 'jobtitle turnstileLink')
# print(len(a_links))
# print(a_links[0])
a_link = a_links[0]
href = a_link['href']
title = a_link['title']
print(f"printing href: {href}")
print('_________________')
print(f"printing title: {title}")

# soup.find('a')['href']
# for job in job_result:
#     title = job.get('title')
#     print(title)
#     print('_______________')


# jobtitle is a class which is associated to open positions
# jobtitle = results.findAll('a', {'class' : 'jobtitle'})
# for title in jobtitle:
    # print(title.prettify())
    # print('_______________')
    # prints the <a> elements with the class jobtitle

# finds job titles 15
job_result = soup.findAll('a', {'class': 'jobtitle'})
# for job in job_result:
#     title = job.get('title')
#     print(title)
#     print('_______________')

# finds when annonce posted
# date_result = soup.findAll('span', {'class': 'date'})
# for date in date_result:
    # print(date.text)
# print(date_result)

# jobtitle2 = soup.findAll('a', {'class': 'turnstileLink'},)
# for job in jobtitle2:
#     print(job.text) # I tried to see companies as they are in <a> tag's text field...But I get againg the job positions

jobtitle2 = soup.findAll('a')
print(len(jobtitle2))
print(jobtitle2[100])

# gives me 15 locations
# locations = results.find_all(['div', 'span'], {'class' : 'location'})
# for location in locations:
# print(location.text)