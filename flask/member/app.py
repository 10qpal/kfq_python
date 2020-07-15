from flask import Flask, request, render_template, redirect, jsonify, url_for
import pymysql, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usersform', methods=['GET', 'POST'])
def usersform():
    if request.method == 'GET':     # 링크를 타고 넘어갔기 때문에 GET 방식 : 가져오는 것(상태를 안 바꿈)
        return render_template('usersform.html')
    else:       # 정보 입력받고 submit 버튼을 누르는 것은 POST 방식 : 수행하는 것(상태를 바꿈)
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        username = request.form.get('username')
        userage = request.form.get('userage')
        useremail = request.form.get('useremail')
        useradd = request.form.get('useradd')
        usergender = request.form.get('usergender')
        usertel = request.form.get('usertel')

        try:
            connection = pymysql.connect(host='localhost', user='root', password='qwer1234', 
            db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                sql = "INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                data = (userid,userpw,username,userage,useremail,useradd,usergender,usertel)
                cursor.execute(sql,data)
                connection.commit()

        finally:
            connection.close()

    return redirect('/list')

@app.route('/list')
def list():
    connection = pymysql.connect(host='localhost', user='root', password='qwer1234', 
    db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)

    finally:
        connection.close()

    return render_template('list.html', list=result)

@app.route('/content/<userid>')
def content(userid):
    connection = pymysql.connect(host='localhost', user='root', password='qwer1234', 
    db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE userid = %s"
            cursor.execute(sql, userid)
            result = cursor.fetchone()
            # print(result)

    finally:
        connection.close()

    return render_template('content.html', list=result)

@app.route('/updateform/<userid>', methods=['GET'])
def updateformget(userid):
    connection = pymysql.connect(host='localhost', user='root', password='qwer1234', 
    db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE userid = %s"
            cursor.execute(sql, userid)
            result = cursor.fetchone()
            # print(result)

    finally:
        connection.close()

    return render_template('updateform.html', list=result)

@app.route('/updateform', methods=['POST'])
def updateformpost():
    connection = pymysql.connect(host='localhost', user='root', password='qwer1234', 
    db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    userid = request.form.get('userid')
    userpw = request.form.get('userpw')
    username = request.form.get('username')
    userage = request.form.get('userage')
    useremail = request.form.get('useremail')
    useradd = request.form.get('useradd')
    usergender = request.form.get('usergender')
    usertel = request.form.get('usertel')

    try:
        with connection.cursor() as cursor:
            sql = '''
            UPDATE users SET
            userpw=%s,
            username=%s,
            userage=%s,
            useremail=%s,
            useradd=%s,
            usergender=%s,
            usertel=%s
            WHERE userid=%s
            '''
            data = (userpw,username,userage,useremail,useradd,usergender,usertel,userid)
            cursor.execute(sql,data)
            connection.commit()

    finally:
        connection.close()

    return redirect('/list')

@app.route('/deleteform/<userid>')
def deleteformget(userid):
    connection = pymysql.connect(host='localhost', user='root', password='qwer1234', 
    db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM users WHERE userid = %s"
            cursor.execute(sql, userid)
            connection.commit()

    finally:
        connection.close()

    return redirect('/list')

@app.route('/ajaxlist')
def ajaxlistget():
    connection = pymysql.connect(host='localhost', user='root', password='qwer1234', 
    db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            result = cursor.fetchall()
            
    finally:
        connection.close()
    
    return render_template('ajaxlist.html', list=result)

@app.route('/ajaxlist', methods=['POST'])
def ajaxlistpost():
    connection = pymysql.connect(host='localhost', user='root', password='qwer1234', 
    db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    userid = request.form.get('userid')

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE userid like %s"
            userid = '%'+userid+'%'
            cursor.execute(sql, userid)
            result = cursor.fetchall()

    finally:
        connection.close()

    return jsonify(result)

@app.route('/imglist')
def imglist():
    # print(os.path.dirname(__file__))
    dirname = os.path.dirname(__file__)+'/static/img/'
    filenames = os.listdir(dirname)
    # print(filenames)
    return render_template('imglist.html', filenames=filenames)

if __name__ == '__main__':
    app.run(debug=True)