import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")       # id/password@server:host/xe
c = conn.cursor()

sql = 'SELECT * FROM employees'
c.execute(sql)
for row in c:
    print(row)

conn.close()