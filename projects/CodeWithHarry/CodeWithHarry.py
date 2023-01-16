# if you want to scrape a website:
# 1. Use the API
# 2.HTML Web Scraping using some tools like bs4

# step 0: install needed requirements
# pip install request
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/"
# step 1: get the html
r = requests.get(url)
htmlContent = r.content
# print(htlContent)

# step 2: parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# step 3: Tree traversal the html
#
# commonly used types of objects:
# 1. Tag
# print(type(title))
# 2.NavigableString
# print(type(title.string))
# 3. BeautifulSoup
# print(type(soup))
# 4. Comment


#  get title
title = soup.title
# print(title)

# get all paragraphs
paras = soup.find_all('p')
# print(paras)

print(soup.find('p'))  # to print first one paragraph
print(soup.find('p')['class'])  # to print first one paragraph with class

# find all the elements with class lead
print(soup.find_all("p", class_="lead"))

# get the text from the tags/soup
print("texts are: ", soup.find('p').get_text())

#  get all anchors
anchors = soup.find_all('a')
all_links = set()
#  get all links on the page
for link in anchors:
    if (link.get('herf') != '#'):
        linkText = "https://www.codewithharry.com/" + link.get('href')
        all_links.add(link)
        print(linkText)
        # print(link.get('href'))

# comments
markup = "<p><!-- this is comment --></p>"
soup2 = BeautifulSoup(markup)
print("comments:", soup2.p.string)
print("comments:", type(soup2.p.string))
exit()
