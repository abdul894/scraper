from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_unicorn_startup_companies"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)