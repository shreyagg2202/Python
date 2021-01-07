import  sqlite3

con = sqlite3.connect("MYFORM1.db")

cursor = con.cursor()

#cursor.execute("create table st(id integer,Name text,Age integer)")

#cursor.execute("insert into st values(1,'Shrey',19)")

#cursor.execute("create table st(:id,:Name,:Age)",{'id':2,'Name':'Shrey','Age':19})

#cursor.executemany("insert into st values(?,?,?)",[(3,'abc',22),(4,'ABC',26)])

con.commit()
con.close()
