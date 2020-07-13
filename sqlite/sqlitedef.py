import sqlite3

# 커넥션
def create_conn():
    conn = sqlite3.connect('sqlite/my_books.db')
    return conn
# 커서는 열고 닫는 문제 때문에 함수로 만들기 애매함

# 테이블 생성 함수
def create_table():
    with create_conn() as conn:     # with 문 빠져나가면 자동으로 종료되는 특성 이용
        c = conn.cursor()

        sql = ('''
        CREATE TABLE if not exists books(
            title text,
            published_date text,
            publisher text,
            pages integer,
            recommend integer)
            ''')
        c.execute(sql)
        conn.commit()

        c.close()

# 데이터 입력 함수
def insert_book(item):
    conn = create_conn()
    c = conn.cursor()

    sql = 'INSERT INTO books VALUES (?,?,?,?,?)'
    c.execute(sql, item)
    conn.commit()

    c.close()
    conn.close()

def insert_books(items):
    conn = create_conn()
    c = conn.cursor()

    sql = 'INSERT INTO books VALUES (?,?,?,?,?)'
    c.executemany(sql, items)
    conn.commit()

    c.close()
    conn.close()

def all_books():
    conn = create_conn()
    c = conn.cursor()

    sql = 'SELECT * FROM books'
    c.execute(sql)
    books = c.fetchall()
    # print(type(books))      # list
    print(books)
    return books

    c.close()
    conn.close()

def one_book(title):
    conn = create_conn()
    c = conn.cursor()

    sql = 'SELECT * FROM books WHERE title = ?'     # 일부 일치 : like 이용
    c.execute(sql, title)
    book = c.fetchone()     # PK로 검색했다고 가정하고 하나만 출력되도록
    return book

    c.close()
    conn.close()

def one_book_id(id):
    conn = create_conn()
    c = conn.cursor()

    sql = 'SELECT * FROM books WHERE rowid = ?'
    c.execute(sql, id)
    book = c.fetchone()
    return book

    c.close()
    conn.close()


def select_book(title):
    conn = create_conn()
    c = conn.cursor()

    sql = 'SELECT * FROM books WHERE title like ?'     # 일부 일치 : like 이용
    title = "%"+title+"%"
    c.execute(sql, (title,))        # 튜플 처리
    book = c.fetchone()     # PK로 검색했다고 가정하고 하나만 출력되도록
    return book

    c.close()
    conn.close()



if __name__ == '__main__':   
    create_table()

    # item = ('데이터 분석 실무','2020-07-13','위키북스',300,10)
    # insert_book(item)
    # items = [
    #     ('빅데이터','2020-07-15','이지스퍼블리싱',600,50),
    #     ('안드로이드','2020-07-17','삼성',120,30),
    #     ('스프링','2020-07-20','위키북스',500,20)
    # ]
    # insert_books(items)

    # all_books()

    # one_book()
    book = one_book(('안드로',))       # 입력을 튜플 형태로
    print(book)
    book = one_book_id((1,))
    print(book)
    book = select_book('빅데')      # 그냥 입력을 받고 함수 안에서 튜플 형태로
    print(book)

