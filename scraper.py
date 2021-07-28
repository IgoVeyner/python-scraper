import requests
from bs4 import BeautifulSoup

# Simple web scraper that scrapes polygon.com and lists all article names / links

URL = "https://www.polygon.com/"
page = requests.get(URL)


if page.status_code == 200:
  print ("Articles\n---")
  soup = BeautifulSoup(page.content, "html.parser")
  articles = [item for item in soup.find_all('a', attrs={'data-analytics-link': "article"})]

  for i, article in enumerate(articles):
    print (i, ": ", article.text, "\n", article["href"], "\n---")

else:
  print ("error" + page.status_code)
