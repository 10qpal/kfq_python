import pymysql

def create_conn():
    conn = pymysql.connect(host='localhost', user='root', password='qwer1234',
    db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()   

# 테이블 생성 함수
def create_table():
    conn = create_conn()
    c = conn.cursor()

    sql = ('''
    CREATE TABLE if not exists books(
        book_id integer NOT NULL AUTO_INCREMENT PRIMARY KEY,
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer)
        DEFAULT CHARSET=utf8
        ''')
    c.execute(sql)
    conn.commit()
    c.close()

# 데이터 입력 함수(한 건)
def insert_book(item):
    conn = create_conn()
    c = conn.cursor()

    sql = 'INSERT INTO books VALUES (book_id,%s,%s,%s,%s,%s)'
    c.execute(sql, item)
    conn.commit()
    c.close()

# 데이터 입력 함수(여러 건)
def insert_books(items):
    conn = create_conn()
    c = conn.cursor()

    sql = 'INSERT INTO books VALUES (book_id,%s,%s,%s,%s,%s)'
    c.executemany(sql, items)
    conn.commit()
    c.close()       

# 전체 데이터 가져오기
def all_books():
    conn = create_conn()
    c = conn.cursor()

    sql = 'SELECT * FROM books'
    c.execute(sql)
    books = c.fetchall()
    print(books)
    return books
    c.close()

# 한 건의 데이터 가져오기(book_id)
def one_book_id():
    conn = create_conn()
    c = conn.cursor()

    choose_id = input("책 번호 입력 : ")
    sql = 'SELECT * FROM books WHERE book_id = %s'
    c.execute(sql, choose_id)
    book = c.fetchone()
    print(book)
    return book
    c.close()

# 한 건의 데이터 가져오기(title)
def one_book_title():
    conn = create_conn()
    c = conn.cursor()

    choose_title = input("책 제목 입력(일부분도 가능) : ")
    sql = 'SELECT * FROM books WHERE title like %s'
    choose_title = "%"+choose_title+"%"
    c.execute(sql, choose_title)
    book = c.fetchone()
    print(book)
    return book
    c.close()

def update_title():
    conn=create_conn()
    c=conn.cursor()

    find_id = int(input("내용을 수정할 책 번호 입력 : "))
    update_title = str(input("새로운 책 제목 입력 : "))
    data=(find_id, update_title)
    sql='''UPDATE books
            SET title = %s WHERE book_id = %s'''
    c.execute(sql, data)
    conn.commit()
    c.close()

def delete_book(id):
    conn=create_conn()
    c=conn.cursor()

    delete_id = input("삭제할 책 번호 입력 : ")
    sql='DELETE FROM books WHERE book_id = %s'
    c.execute(sql, delete_id)
    conn.commit()
    c.close()

if __name__ == '__main__':
    while True:
        choice=input('''
        다음 중에서 하실 일을 골라주세요 :
        A - 테이블 생성  
        B - 전체 데이터 가져오기
        C - 한 건의 데이터 가져오기(book_id)
        D - 한 건의 데이터 가져오기(title)
        E - 데이터 수정하기(제목 수정)
        F - 데이터 삭제하기
        Q - 프로그램 종료
        ''').upper()

        if choice=='A':
            create_table()
        elif choice=='B':
            all_books()
        elif choice=='C':
            one_book_id()
        elif choice=='D':
            one_book_title()
        elif choice=='E':   
            update_title() 
        elif choice=='F':   
            delete_book()          
        elif choice=='Q':
            quit() 



    # create_table()

    # item = ('데이터 분석 실무','2020-07-13','위키북스',300,10)
    # insert_book(item)
    # items = [
    #     ('빅데이터','2020-07-15','이지스퍼블리싱',600,50),
    #     ('안드로이드','2020-07-17','삼성',120,30),
    #     ('스프링','2020-07-20','위키북스',500,20)
    # ]
    # insert_books(items)

    # all_books()

    # one_book_id()
    # one_book_title()
