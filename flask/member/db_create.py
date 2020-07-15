import pymysql      # mariaDB

# 딕셔너리 형태로 쓰겠다, cursorclass 설정 안 하면 기본은 튜플 형태
connection = pymysql.connect(host='localhost', user='root', password='qwer1234',
db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = 'DROP TABLE if exists users'
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        # VARCHAR(20) : 가변 길이(20자 미만인 경우 알아서 맞춰준다)
        sql = '''
        CREATE TABLE if not exists users(
            userid VARCHAR(20) PRIMARY KEY,
            userpw VARCHAR(20) NOT NULL,
            username VARCHAR(20) NOT NULL,
            userage INT,
            useremail VARCHAR(20),
            useradd VARCHAR(50),
            usergender VARCHAR(20),
            usertel VARCHAR(20)
        ) DEFAULT CHARSET=utf8
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = '''
        INSERT INTO users VALUES(
            'gildong1','1234','길동',33,'gildong@gmail.com','부산시 남구','male','010-1234-1234'
        )
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = 'SELECT * FROM users'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()