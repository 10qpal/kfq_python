import sqlite3

conn = sqlite3.connect('sqlite/example.db')
c = conn.cursor()

# Never do this -- insecure!
# symbol = 'RHAT'
# c.execute('''
# SELECT * FROM stocks
# WHERE symbol = '%s'
# '''%symbol)

# Do this instead
# t = ('RHAT',)       # 튜플에 값 하나 넣을 때는 뒤에 ,(콤마) 붙여야 함
# sql = 'SELECT * FROM stocks WHERE symbol = ?'
# c.execute(sql, t)       # c.execute(sql, (t,t1))

# print(c.fetchall())     # fetchone : 하나만 가져옴 / fetchall : 모두 가져옴



# Larger example that inserts many records at a time
# items = [('2020-07-09', 'BUY', 'IBM', 1000, 45.00),
# ('2020-07-10', 'SELL', 'MSFT', 500, 72.00),
# ('2020-07-11', 'BUY', 'IBM', 800, 53.00),
# ('2020-07-12', 'SELL', 'RHAT', 100, 90.00)]

# sql = "INSERT INTO stocks VALUES (?,?,?,?,?)"       # 위치만 잡아주면 된다, 따옴표 신경 안 써도 됨
# c.executemany(sql, items)       # 한 번에 여러 개 실행, 반복문 실행하는 것보다 속도가 더 빠르다
# conn.commit()     # INSERT문 : commit 반드시

sql2 = "SELECT * FROM stocks ORDER BY price"
c.execute(sql2)
rows = c.fetchall()

# print(type(rows))     # 리스트
print(rows)
for row in rows:
    # print(type(row))      # 튜플
    print(row)
    # print(row[0])     # 날짜만 출력

# for row in c.execute(sql2):       # 같은 동작
#     print(row)



c.close()
conn.close()