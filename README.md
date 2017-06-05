# Web-Scraping

The easiset way to scrape data from web is by using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/).

# Getting Start
#### Creating Virtual Enviornment
You can use [Anaconda](https://www.continuum.io/downloads) to create a new virtual Enviornment([docs](https://conda.io/docs/using/envs.html)).

#### Install the tools in a new virtualenv:

```
pip install beautifulsoup4
pip install requests
```

# Start Scraping

Lets scrape real time data from [Hacker News](https://news.ycombinator.com/)

```
>>> import requests
>>>
>>> response = requests.get("https://news.ycombinator.com/")
>>>
>>> response.status_code
>>> 200
```

Make sure you got the status code 200.

Store the response in other variable

```
>>> data = response.content
```
Start parsing with Beautiful Soup

```
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(data,'html.parser')
>>> samples = soup.find_all("a","storylink")
>>> news = list(samples)
>>> print(len(news))
>>> 30
>>> print(news[0].contents)
>>> ['Oculus founder Palmer Luckey is developing border surveillance technology']
```
Use for loop to print all 30 stories.

```
>>> for i in news:
...    print(i.contents)
```

Learn more about Beautiful Soup, Here are some [online docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

Now You are ready to scrape any real time data, Now Go and scrape :)
