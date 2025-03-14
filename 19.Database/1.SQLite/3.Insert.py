import sqlite3

con = sqlite3.connect('Details_db')


sql = """
INSERT INTO Details_tb VALUES
(4, 'Libin', 13), (5, 'Manu', 14),
(6, 'Anju', 12)
"""

con.execute(sql)

con.commit()

con.close()

