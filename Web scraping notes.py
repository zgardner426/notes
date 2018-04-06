# Web scraping


from bs4 import BeautifulSoup
import requests
import random
'''
for i in range(1, 11):
    url = "http://quotes.toscrape.com/page/" + str(i)

page = requests.get(url)
#print(page.text)

soup = BeautifulSoup(page.text, "html.parser") #html. parser is the defult so if you don't include it it's fine
#print(soup.prettify())

#findAll - search by tag name, attribute(kwarg), class(kwarg), string=""
quotes = soup.findAll("span", class_="text")
#print(quotes)

for quote in quotes:
    print(quote.text)

authors = soup.findAll("small", class_="author")

for author in authors:
    print(author.text)

for i in range(len(quotes)):
    print(quotes[i].text, authors[i].text)
'''

url = "https://www.regmovies.com/theaters/regal-webster-place-11/C00129681357"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

titles = [x.text.strip() for x in soup.findAll("h3", class_="title")]
print(titles)

showtimes = [x.findAll("li", class_="showtime-entry") for x in soup.findAll("ul", class_="format-showtimes")]

for i in range(11):
    print("\n\n")
    print(titles[i])
    for j in range(len(showtimes[i])):
        print(showtimes[i][j].text)