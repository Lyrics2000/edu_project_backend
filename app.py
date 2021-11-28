# importing the libraries

from bs4 import BeautifulSoup

import requests

url="https://www.scholars4dev.com/tag/scholarships-for-kenyans/"
# Make a GET request to fetch the raw HTML content

html_content = requests.get(url).text


# Parse the html content

soup = BeautifulSoup(html_content, "lxml")

mydivs = soup.find_all("div", {"class": "entry"})
for v in mydivs:
    print(v)