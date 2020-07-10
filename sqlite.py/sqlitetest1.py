import sqlite3

conn = sqlite3.connect('example.db')    # DB 연결(파일명만 작성)

c = conn.cursor()     # 커서 리턴

# Create table
# c.execute('''
# create table stocks(data text, trans text, symbol text, qty real, price real)
# ''')

c.execute("insert into stocks values ('2020-07-08','BUY','RHAT',100,35.14)")

conn.commit()
conn.close()