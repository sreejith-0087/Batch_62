import pymysql  #pip install pymysql

con = pymysql.connect(host='localhost', user='root', password='', db='details_db')

c = con.cursor()

sql = "INSERT INTO details_tb(Id, Name, Subject, Phone) VALUES (2, 'Manu', 'English', 98357357258)"

c.execute(sql)

con.commit()

