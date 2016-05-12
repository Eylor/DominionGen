import urllib.request
import sqlite3
from bs4 import BeautifulSoup

def urlToSoup(url):
#open URL w/ URLLIB & soup
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, "html.parser")
	return soup

def soupToDB(url):
	#select card table
	for tr in urlToSoup(url).find_all('tr'):
		tds = tr.find_all('td')
		#saving data
		name = tds[0].text
		types = tds[1].text#.encode('UTF-8').decode("ascii", errors="ignore")
		cost = tds[2].text
		effect = tds[3].text
		#insert data into db
		conn.execute("INSERT INTO Cards VALUES (?, ?, ?, ?);", (name, types, cost, effect))
		conn.commit()

#create or open db
conn = sqlite3.connect('DominionCards.db')
print("Opened database success")

#create db table
conn.execute("CREATE TABLE Cards (Name TEXT NOT NULL, Types TEXT NOT NULL, Cost INT NOT NULL, Effect TEXT NOT NULL);")
print('Table created successfully')

#URLs
dominionURL = "https://dominionstrategy.com/card-lists/dominion-card-list/"
intrigueURL = "https://dominionstrategy.com/card-lists/intrigue-card-list/"
prosperityURL = "https://dominionstrategy.com/card-lists/prosperity-card-list/"

#scrape each page and enter in DB
soupToDB(dominionURL)
soupToDB(intrigueURL)
soupToDB(prosperityURL)
	
print("records created")
conn.close()