import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'

session = requests.Session()

response = session.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
content = soup.find_all(class_='text')

for item in content:
    text = item.get_text()
    print()
    print(text)
    print()