import pymysql

conn = pymysql.connect(host='localhost', user='root', password='qwer1234',
db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
c = conn.cursor()

sql = '''CREATE TABLE if not exists stocks (
    data text, trans text, symbol text, qty real, price real
    )'''
c.execute(sql)

sql2 = "INSERT INTO stocks VALUES ('2020-07-08','BUY','RHAT',100,35.14)"
c.execute(sql2)

conn.commit()

conn.close()        # 커넥션 클로즈하면 커서 클로즈는 자동으로 수행