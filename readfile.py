import sqlite3


conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()


texts = open('ProductCatalogue.txt','r+')
content = texts.readline()
contents = texts.readlines()
# print(contents)

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS Devices(device_type TEXT, brand_name TEXT,ram TEXT,storage_size TEXT,screen_size TEXT,cost INTEGER,supplier TEXT)')


def populate_db():
	i = 1
	for line in contents:
		line = line.split(";")
		c.execute('INSERT INTO sarpenstein_device  Values(?,?,?,?,?,?,?,?)',(i,line[0],line[1],line[2],line[3],line[4],line[5],line[6],))
		i+=1
		conn.commit()


#create_table()
populate_db()
# c.close()x
#conn.close()