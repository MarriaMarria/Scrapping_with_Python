import requests
import pprint
from bs4 import BeautifulSoup

# This code performs an HTTP request to the given URL. It retrieves the 
# HTML data that the server sends back and stores that data in a Python object.


URL = 'https://fr.indeed.com/jobs?q=Developpeur+Cloud&l=Paris+%2875%29'
page = requests.get(URL)
# pprint.pprint(page.content)

# soup = BeautifulSoup(page.content, 'html.parser')
soup = BeautifulSoup(page.content, 'lxml')

# taking the div with all results
results = soup.find(id='resultsCol')
# print(results.prettify())

# jobtitle is a class which is associated to open positions
# jobtitle = results.findAll('a', {'class':'jobtitle'})
# for title in jobtitle:
    # print(title.prettify())
    # print('_______________')


# finds job titles 15
# job_result = soup.findAll('a', {'class': 'jobtitle'})
# for job in job_result:
#     title = job.get('title')
#     # print(title)
#     # print('_______________')

# # finding date 15
# date_result = soup.findAll('span', {'class': 'date'})
# for date in date_result:
#     print(date.text)
# # print(date_result)

# not good as prints both company names smtimes and position
# jobtitle2 = soup.findAll('a', {'class': 'turnstileLink'},)
# print(jobtitle2)
# for each in jobtitle2: 
#     print (str(each.get_text()))
    #prints again jobtitles


# company = jobtitle2.a.text
# print(company)
# for job in jobtitle2:
#     title = job.get('title')
#     print(title)
#     print('_______________')

# 1st file with urls

# df = pd.DataFrame(data={"href": list_hrefs})
# df.to_csv("data_file_3.csv", sep=',',index=False)

# # 2nd file with id:s and labels

# pairs = {'id': list_ids, 'label': list_labels}
# df = pd.DataFrame.from_dict(pairs)
# df.to_csv('ids_labels_3.csv')
