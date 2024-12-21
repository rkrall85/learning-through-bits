

import requests
import bs4

res = requests.get('http://www.example.com')

#print(type(res))

#print(res.text) #output text on website


soup = bs4.BeautifulSoup(res.text,'lxml')

#print(soup)
#print(soup.select('title')) #only output title of website
title_tag_list = soup.select('title')
print(title_tag_list[0].getText())
