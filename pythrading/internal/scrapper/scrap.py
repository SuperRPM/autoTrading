import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/item/main.nhn?code=000660").text

soup = BeautifulSoup(response, "html.parser")
tags = soup.select("#_per")
tag = tags[0]
for tag in tags:
    print(tag.text)
