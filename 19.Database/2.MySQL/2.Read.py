import pymysql

con = pymysql.connect(host='localhost', user='root', password='', db='details_db')

c = con.cursor()

sql = "SELECT * FROM details_tb"

c.execute(sql)

new = c.fetchall()

for i in new:
    print(f'{i[0]} | {i[1]} | {i[2]} | {i[3]}')
    con.commit()

