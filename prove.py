import requests
from bs4 import BeautifulSoup
url = 'https://www.goodreads.com/book/show/2767052-the-hunger-games'

page = requests.get(url).text

soup = BeautifulSoup(page)
print(soup.prettify())