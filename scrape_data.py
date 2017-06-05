import requests

response = requests.get("https://news.ycombinator.com/")

data = response.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(data,'html.parser')
samples = soup.find_all("a","storylink")
news = list(samples)
for i in news:
    print(i.contents)

