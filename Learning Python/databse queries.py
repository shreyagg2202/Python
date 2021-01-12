import sqlite3

con = sqlite3.connect("MYFORM1.db")

cursor = con.cursor()

cursor.execute("select* from st")
#print(cursor.fetchone())
#print(cursor.fetchall())
#print(cursor.fetchmany(2))
#cursor.execute("delete from st where id = 3")
con.commit()
con.close

