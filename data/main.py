import requests
from bs4 import BeautifulSoup
import sqlite3

# in scrapping class
# href_list = []
# title_list = []
# locations_list = []
# date_lists = []


conn = sqlite3.connect('scrapping.db') #connection
c = conn.cursor() # to execute sql commands

# creates table

# c.execute("""CREATE TABLE job_offers (
#             job_title text, 
#             company text, 
#             location text, 
#             published text
#             )""")

# insert a row of data
# for x in range(0, len(title_list)):
#     c.execute("INSERT INTO job_offers VALUES (?, ?, ?, ?)", (href_list[x], title_list[x], locations_list[x], date_list[x]))

c.execute("SELECT * FROM job_offers")

# save (commit) the changes
conn.commit()
conn.close()
# 
# # close of finished, but make sure that changes are committed


URL = 'https://fr.indeed.com/emplois?q=developpeur+web&l=Paris+%2875%29'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# taking the div with all results
results = soup.find(id='resultsCol')
a_links = results.find_all('a', class_ = 'jobtitle turnstileLink')
# print(len(a_links))
# print(a_links[0])
# a_link = a_links[0]
# href = a_link['href']
# title = a_link['title']
# print(f"printing href: https://indeed.fr{href}")
# print('_________________')
# print(f"printing title: {title}")



for link in a_links:
    href = link.get('href')
    href_list.append(href)
    # print(f"Href is: https://indeed.fr{href}")
    # print()
    title = link.get('title')
    title_list.append(title)
    # print(f"Job title is: {title}")
    # print('_______________')

locations = results.find_all(['div', 'span'], {'class' : 'location'})
for location in locations:
    # print(location.text)
    # print('_______________')
    locations_list.append(location.text)

# finds when annonce posted
date_result = results.findAll('span', {'class': 'date'})
for date in date_result:
    # print(date.text)
    date_lists.append(date.text)
    # print('********')
#print(date_result)

print(title_list)
print('____________')
print(href_list)
print('____________')
print(locations_list)
print('____________')
print(date_lists)
print('____________')

