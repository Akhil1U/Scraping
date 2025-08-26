# 7. Extract a Table from Wikipedia

# Goal: From https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal) extract all rows of the first table.

# ✅ What to use: .find('table'), .find_all('tr'), .find_all('td')

import requests
from bs4 import BeautifulSoup

headers = {
    "Accept":"image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
}

session = requests.Session()

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

response = session.get(url,headers=headers)
print(response.status_code)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("table", {"class": "wikitable"})



# Iterate over rows (skip the header row)
    for row in table.find_all("tr")[1:]:
        td = row.find("td")  # first contains country name
        if td:
            a = td.find("a")
            if a:
                print((a.get_text(strip=True)))
                print()
   

else:
    print("not valid status code.....")

# print(countries[:20])  # print first 20 countries
