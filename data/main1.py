import requests
import pprint
from bs4 import BeautifulSoup
import sqlite3

URL = 'https://fr.indeed.com/emplois?q=developpeur+web&l=Paris+%2875%29'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')
a_links = results.find_all('a', class_ = 'jobtitle turnstileLink')

db = sqlite3.connect("scrap.db")
cursor = db.cursor()
# cursor.execute("CREATE TABLE offers (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL, company varchar(250) NOT NULL, location varchar(250) NOT NULL, published varcher(250))")
# db.commit()

title_list = []
locations_list = []
date_lists = []
href_list = []

for x in range(0, len(title_list)):
    cursor.execute("INSERT INTO offers VALUES (?, ?, ?, ?, ?)", (null, title_list[x], href_list[x], locations_list[x], date_lists[x]))
    x = x + 1
    
db.commit()
db.close()



# creates table

def find_and_store_links():

    for link in a_links:
        href = link.get('href')
        href_list.append(href)
    # print(f"Href is: https://indeed.fr{href}")
    # print('_______________________________')



def find_and_store_titles():

    for title in a_links:
        title = title.get('title')
        title_list.append(title)
        return title_list
            #print(f"Job title is: {title}")


def find_locations():

    locations = results.find_all(['div', 'span'], {'class': 'location'})
    for location in locations:
        locations_list.append(location.text)
        return locations_list
    #print(locations_list)


# finds when annonce posted
def date_when_posted():

    date_result = results.findAll('span', {'class': 'date'})
    for date in date_result:
        date_lists.append(date.text)
        return date_lists

# print(href_list)
    # fetch the data

# def select_from_db():

#     db = sqlite3.connect('scrap.db') 
#     db = db.cursor() 

#     db.execute("SELECT * FROM offers")
#     fetched = db.fetchall()
#     print("Total rows are:  ", len(fetched))
#     print("Printing each row")
# #     for row in fetched:
# #         print("Title: ", row[0])
# #         print("Company: ", row[1])
# #         print("Location: ", row[2])
# #         print("Published: ", row[3])
# #         print("Published: ", row[3])
# #         print("\n")

#     db.commit()
#     db.close()
# #     return fetched

# # #insert_data()
# select_from_db()
# # #create_db()