import sqlite3

def insertdata(data):
	rowId = 0
	db = sqlite3.connect('test.db')
	print("Opened database Succesfully")

	query = "INSERT INTO criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
             data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"],
             data["Nationality"], data["Religion"], data["Crimes Done"])

    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("data stored on row %d" % rowId)
    except:
        db.rollback()
        print("Data insertion failed")

    db.commit()
	print ("Records created successfully");
	db.close()
	return rowId

# 	# db.execute("INSERT INTO criminaldata (ID,NAME,FATHER NAME,MOTHER NAME,GENDER,DOB,BLOOD GROUP,IDENTIFICATION MARK,NATIONALITY,RELIGION,CRIMES) \
# 	#       VALUES (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"],data["Nationality"], data["Religion"], data["Crimes Done"])");

# db.commit()
# print "Records created successfully";
# db.close()


# import sqlite3

# conn = sqlite3.connect('test.db')
# print "Opened database successfully";

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

# conn.commit()
# print "Records created successfully";
# conn.close()