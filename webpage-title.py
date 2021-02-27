import requests
from bs4 import BeautifulSoup
page = requests.get("https://github.com/ineelhere")
soup = BeautifulSoup(page.text, "html.parser")
print(f"Title of the page is - {soup.title.string}")
