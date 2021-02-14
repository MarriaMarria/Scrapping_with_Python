import requests
import pprint
from bs4 import BeautifulSoup
import sqlite3

URL = 'https://fr.indeed.com/emplois?q=developpeur+web&l=Paris+%2875%29'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')
a_links = results.find_all('a', class_ = 'jobtitle turnstileLink')

db = sqlite3.connect("scrapIt.db")
cursor = db.cursor()
# cursor.execute("CREATE TABLE jobOffers (title varchar(100), company varchar(50), location varchar(50), published varcher(50), more info varchar(250))")
# db.commit()

title_list = []
locations_list = []
date_lists = []
href_list = []
company_list = []


def find_companies():
    companies = results.find_all('span', class_ = 'company')
    for company in companies:
        text = company.getText()
        text2 = text.strip()
        print(text2)
        company_list.append(text2)
        print(company_list)
# find_companies()




def find_and_store_links():

    for link in a_links:
        href = link.get('href')
        href = "https://indeed.fr" + href
        href_list.append(href)
    return href_list
    print(href_list)

# find_and_store_links()


def find_and_store_titles():

    for title in a_links:
        title = title.get('title')
        title_list.append(title)

    return title_list
    print(title_list)

def find_locations():

    locations = results.find_all(['div', 'span'], {'class': 'location'})
    for location in locations:
        locations_list.append(location.text)
    return locations_list
    print(locations_list)


def date_when_posted():

    date_result = results.findAll('span', {'class': 'date'})
    for date in date_result:
        date_lists.append(date.text)
    return date_lists
    print(date_lists)

# find_companies()
# find_and_store_links()
# find_and_store_titles()
# find_locations()
# date_when_posted()
# print(href_list)


def insert_data():
    db = sqlite3.connect('scrapIt.db') 
    cursor = db.cursor() 

    for x in range(0, len(title_list)):
        # cursor.execute("""INSERT or REPLACE INTO {} VALUES ({}, "{}", "{}");""".format(title_list[x], href_list[x], locations_list[x], date_lists[x]))
        # x = x + 1
        # print(title_list)
        cursor.execute("INSERT or REPLACE INTO jobOffers VALUES (?, ?, ?, ?, ?)", (title_list[x], company_list[x], locations_list[x], date_lists[x], href_list[x]))
        x = x + 1

    db.commit()
    db.close()

# insert_data()

# fetch the data

def select_from_db():

    db = sqlite3.connect('scrapIt.db') 
    cursor = db.cursor() 

    cursor.execute("SELECT * FROM jobOffers")
    fetched = cursor.fetchall()
    print("Total rows are:  ", len(fetched))
    print("Printing each row")
    for row in fetched:
        print("Title: ", row[0])
        print("Company: ", row[1])
        print("Location: ", row[2])
        print("Published: ", row[3])
        print("More info: ", row[4])
        print("\n")

    db.commit()
    db.close()
    return fetched


select_from_db()



















        
# db.commit()
# db.close()







# print(href_list)


# # #insert_data()
# select_from_db()
# # #create_db()