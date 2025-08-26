# 6. Scrape Book Titles

# Goal: Go to http://books.toscrape.com/ and extract all book titles from the front page.

# ✅ What to use: soup.select() or .find_all()

import requests
from bs4 import BeautifulSoup

session = requests.Session()

url = "https://books.toscrape.com/catalogue/category/books_1/index.html"

response = session.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Extract the 'src' attribute
for img in soup.find_all('a'):
    src = img.get('title')
    if not src == None:
        print()
        print(src)
        print()
    else:
        pass