import sqlite3

conn = sqlite3.connect('test3.db')

print ("Opened database successfully");

# create table criminaldata(
# id int primary key auto_increment,
# `name` varchar(20) not null,
# `father name` varchar(25),
# `mother name` varchar(25),
# gender varchar(6) not null,
# dob varchar(10),
# `blood group` varchar(5),
# `identity mark` varchar(30) not null,
# nationality varchar(15) not null,
# `religion` varchar(15) not null,
# `crimes` text not null);

# conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
# print "Table created successfully";

conn.execute('''CREATE table criminaldata
	(
			id INTEGER  primary key ,
			name varchar(20) not null,
			father name varchar(25),
			mother name varchar(25),
			gender varchar(6) not null,
			dob varchar(10),
			blood_group varchar(5),
			identity mark varchar(30) not null,
			nationality varchar(15) not null,
			religion varchar(15) not null,
			crimes varchar(100) not null);''')
print ("Table created successfully");

conn.execute("INSERT INTO criminaldata (id,name,father name,mother name,gender,dob,blood_group,identity mark,nationality,religion,crimes) \
      VALUES (1, 'Paul', 'California','California','M',2000-02-03,'B','gfdg','Indiam','dvsd','davdszv')");
conn.commit()
print ("Records created successfully");
conn.close()