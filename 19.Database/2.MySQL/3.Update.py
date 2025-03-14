import pymysql

con = pymysql.connect(host='localhost', user='root', password='', db='details_db')

c = con.cursor()


id = int(input('Enter Id:'))

sql = "update details_tb set Subject='Malayalam' where Id=%d"%id

c.execute(sql)

con.commit()

