import sqlite3

con = sqlite3.connect('Details_db')

cur = con.cursor()
''' Cursor is a Temporary Memory or Temporary Work Station. 
    It is Allocated by Database Server at the Time of Performing DML(Data Manipulation Language) 
    operations on the Table by the User. Cursors are used to store Database Tables. '''

sql = "SELECT * FROM Details_tb"

cur.execute(sql)

print('-'*20)
for (id,name,age) in cur:
    print('| %d | %s | %d |'%(id,name,age))
    print('-' * 20)

cur.close()
con.close()

