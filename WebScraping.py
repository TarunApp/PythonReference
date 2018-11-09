import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup

url = ""

request = requests.get(url)
html_content = request.text

soup = BeautifulSoup(html_content, "html.parser")

print(soup.findAll("div", class_ = "paragraph"))



links = (soup.find_all("a"))
for link in links:
    print(link.get("href"))




