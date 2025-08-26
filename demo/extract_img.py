# 5. Extract All Image URLs

# Goal: Extract all <img> tags and print the src attributes.

# 🔹 Tip: Some images might have relative URLs; use urllib.parse.urljoin() to make full URLs.


import requests
from bs4 import BeautifulSoup

from urllib.parse import urljoin

url = "https://books.toscrape.com/catalogue/category/books_1/index.html"

session = requests.Session()

response = session.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Extract the 'src' attribute
for img in soup.find_all('img'):
    src = img.get('src')
    full_src = urljoin(url,src)
    print(full_src)


