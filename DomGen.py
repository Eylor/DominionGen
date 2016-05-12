import sqlite3
import random

'''
DB Access Key
Name : row[0]
Type : row[1]
Cost : row[2]
Effect : row[3]
'''

#open db
conn = sqlite3.connect('DominionCards.db')
print("Opened database success")

cursor = conn.execute("SELECT name, types, cost, effect from Cards")
cardList = []
for row in cursor:
	if "VP token" not in row[3]:
		if "Platinum" not in row[0]:
			 cardList.append(row[0])

outF = open('outFile.txt', 'w')
outF.write(str(random.sample(cardList, 10)))
#print(random.sample(cardList, 10))
outF.close()
conn.close()
print("done"); 