import requests
import pprint
from bs4 import BeautifulSoup
import sqlite3

href_list = ["href", "href", "href"]
title_list = ["title1", "title2", "title3"]
locations_list = ["loc1", "loc2", "loc3"]
date_lists = ["today", "tomorrow", "yesterday"]

db = sqlite3.connect("try.db")
cursor = db.cursor()
# cursor.execute("CREATE TABLE fuckit (title varchar(250) NOT NULL, company varchar(250) NOT NULL, location varchar(250) NOT NULL, published varcher(250))")
# # # cursor.execute("INSERT or REPLACE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

for x in range(0, len(title_list)):
    cursor.execute("INSERT INTO fuckit VALUES (?, ?, ?, ?)", (title_list[x], href_list[x], locations_list[x], date_lists[x]))
    x = x + 1
    
db.commit()