import sqlite3

con = sqlite3.connect('Details_db')


id = int(input('Enter id:'))

sql = "update Details_tb set age=16 where id=%d"%id


con.execute(sql)

con.commit()

con.close()