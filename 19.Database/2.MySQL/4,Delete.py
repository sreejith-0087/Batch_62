import pymysql

con = pymysql.connect(host='localhost', user='root', password='', db='details_db')

c = con.cursor()

id = int(input('Enter Id:'))

sql = "delete from details_tb where Id=%d"%id

c.execute(sql)

con.commit()
