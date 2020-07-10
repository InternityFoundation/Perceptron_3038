import sqlite3

db = sqlite3.connect('profile.db')
print("Opened database Succesfully")

db.execute('''CREATE TABLE criminaldata
			(ID INTEGER PRIMARY KEY AUTOINCREMENT,
			'NAME' VARCHAR(20) NOT NULL,
			'FATHER NAME' VARCHAR(25),
			'GENDER' VARCHAR(6) NOT NULL,
			'DOB' VARCHAR(10),
			'CRIMES' TEXT NOT NULL);''')

print("Table Created Succesfully")

db.close()