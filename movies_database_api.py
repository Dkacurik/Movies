import requests
import bs4
import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="", db="movies")

i = 1

while i < 10:

    x = str(i)

    res = requests.get('https://www.csfd.cz/film/' + x)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    meno = soup.select('h1')
    myh2 = soup.findAll("h2", {"class": "average"})
    rok = soup.find(itemprop = 'dateCreated')
    year = rok.getText().strip()
    percentage = myh2[0].getText().strip()
    title = meno[0].getText().strip()
    mycursor = conn.cursor()
    mycursor.execute("INSERT INTO csfd(title, percentage, rok_vydania) VALUES (%s, %s, %s)", (title, percentage, int(year)))
    conn.commit()

    print(mycursor.rowcount, "record inserted.")
    i += 1

conn.close

