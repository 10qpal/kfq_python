import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")       # id/password@server:host/xe
c = conn.cursor()

sql = 'SELECT * FROM employees'
c.execute(sql)

sql2 = 'CREATE SEQUENCE book_seq START WITH 1 INCREMENT BY 1'
c.execute(sql2)
sql3 = '''CREATE TABLE books(
    book_id NUMBER NOT NULL,
    title VARCHAR2(50),
    published_date VARCHAR2(50),
    publisher VARCHAR2(50),
    pages NUMBER,
    recommend NUMBER,
    CONSTRAINT pk_book PRIMARY KEY (book_id)
)'''
c.execute(sql3)
item = ('데이터 분석 실무','2020-07-13','위키북스',300,10)
sql4 = '''INSERT INTO books VALUES (
    book_seq.NEXTVAL,:1,:2,:3,:4,:5)'''       # index로 접근
c.execute(sql4, item)
conn.commit()

conn.close()