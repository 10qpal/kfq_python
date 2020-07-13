import pymysql

conn = pymysql.connect(host='localhost', user='root', password='qwer1234',
db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
c = conn.cursor()

items = [('2020-07-09', 'BUY', 'IBM', 1000, 45.00),
('2020-07-10', 'SELL', 'MSFT', 500, 72.00),
('2020-07-11', 'BUY', 'IBM', 800, 53.00),
('2020-07-12', 'SELL', 'RHAT', 100, 90.00)]

sql = "INSERT INTO stocks VALUES (%s,%s,%s,%s,%s)"       # 위치만 잡아주면 된다, 따옴표 신경 안 써도 됨
c.executemany(sql, items)       # 한 번에 여러 개 실행, 반복문 실행하는 것보다 속도가 더 빠르다
conn.commit()     # INSERT문 : commit 반드시

conn.close()