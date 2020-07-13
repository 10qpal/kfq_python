import pymysql

conn = pymysql.connect(host='localhost', user='root', password='qwer1234',
db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
c = conn.cursor()

# t = ('ibm',)
t = ('RHAT',)
sql = "SELECT * FROM stocks WHERE symbol=%s"        # 무조건 %s(sqlite에서의 ?와 같다)

c.execute(sql, t)
print(c.fetchall())     # 딕셔너리 형태(cursorclass에서 그렇게 지정했기 때문에)

conn.close()