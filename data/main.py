import requests
from bs4 import BeautifulSoup
import sqlite3

URL = 'https://fr.indeed.com/emplois?q=developpeur+web&l=Paris+%2875%29'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')
a_links = results.find_all('a', class_ = 'jobtitle turnstileLink')
# print(len(a_links))
# print(a_links[0])
# a_link = a_links[0]
# href = a_link['href']
# title = a_link['title']
# print(f"printing href: https://indeed.fr{href}")
# print(f"printing title: {title}")

href_list = []
title_list = []
locations_list = []
date_lists = []

# creates table

def find_and_store_links():

    for link in a_links:
        href = link.get('href')
        href_list.append(href)
        #print(f"Href is: https://indeed.fr{href}")


def find_and_store_titles():

    for title in a_links:
        title = title.get('title')
        title_list.append(title)
        #print(f"Job title is: {title}")


def find_locations():

    locations = results.find_all(['div', 'span'], {'class': 'location'})
    for location in locations:
        locations_list.append(location.text)
    #print(locations_list)


# finds when annonce posted
def date_when_posted():

    date_result = results.findAll('span', {'class': 'date'})
    for date in date_result:
        date_lists.append(date.text)
    print(date_lists)

def create_db():

    db = sqlite3.connect("my_scraping.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE offers (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL, company varchar(250) NOT NULL, location varchar(250) NOT NULL, published varcher(250))")
    db.commit()
    db.close()


# insert a row of data

def insert_data():

    db = sqlite3.connect('my_scraping.db') 
    cursor = db.cursor() 

    cursor.execute("INSERT or REPLACE INTO offers VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3', 'Herminey')")
    db.commit()
    # for x in range(0, len(title_list)):
    #     c.execute("INSERT INTO job_offers VALUES (?, ?, ?, ?)", (title_list[x], href_list[x], locations_list[x], date_list[x]))
    #     x = x + 1
        # c.execute("""INSERT or REPLACE INTO job_offers VALUES (?, ?, ?, ?)""", ("Web Developper", "https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree", "Paris 75", "3 days ago"))
        
    #     inserted = """INSERT or REPLACE INTO job_offers VALUES (?, ?, ?, ?)""", ("Web Developper", "https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree", "Paris 75", "3 days ago")

    # inserted = """INSERT or REPLACE INTO {} VALUES ({}, "{}", "{}");""".format('Web Developper', 'https://www.crummy.com', 'Paris 75', '3 days ago')
 
    db.close()

# fetch the data

def select_from_db():

    db = sqlite3.connect('scrapping.db') 
    db = db.cursor() 

    db.execute("SELECT * FROM offers")
    fetched = db.fetchall()
    print("Total rows are:  ", len(fetched))
    print("Printing each row")
    for row in fetched:
        print("Title: ", row[0])
        print("Company: ", row[1])
        print("Location: ", row[2])
        print("Published: ", row[3])
        print("Published: ", row[3])
        print("\n")

    db.commit()
    db.close()
    return fetched

#insert_data()
select_from_db()
#create_db()