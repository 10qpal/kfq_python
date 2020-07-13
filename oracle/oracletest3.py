import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")       # id/password@server:host/xe
c = conn.cursor()

# sql = 'SELECT * FROM books WHERE book_id = :id'
# c.execute(sql, id=1)
# print(c.fetchall())

sql = 'SELECT * FROM books WHERE title like :1'
title = "%데이%"
c.execute(sql, (title,))
print(c.fetchall())     # list
# book = c.fetchone()
# print(book)       # tuple

conn.close()