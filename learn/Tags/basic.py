import html5lib
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">TutorialsPoint</b>')
tag = soup.html
type(tag)

xml_soup = BeautifulSoup('<p class="body bold"></p>', 'xml')
