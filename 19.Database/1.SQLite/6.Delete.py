import sqlite3

con = sqlite3.connect('Details_db')


sql = "delete from Details_tb where id=6"

# sql = 'delete from Details_tb'


con.execute(sql)

con.commit()

con.close()

