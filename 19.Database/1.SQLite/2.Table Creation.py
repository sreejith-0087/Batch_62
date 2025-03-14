import sqlite3


con = sqlite3.connect('Details_db')

sql = """
CREATE TABLE Details_tb(
    ID INT PRIMARY KEY,
    NAME TEXT,
    AGE INT
)
"""

con.execute(sql)

con.close()

