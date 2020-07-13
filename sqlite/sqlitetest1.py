import sqlite3

conn = sqlite3.connect('sqlite/example.db')    # DB 연결(경로 작성)

c = conn.cursor()     # 커서 리턴

# Create table
c.execute('''CREATE TABLE if not exists stocks
(data text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2020-07-08','BUY','RHAT',100,35.14)")

# Save(commit) the changes
conn.commit()

conn.close()