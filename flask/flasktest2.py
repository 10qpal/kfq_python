# (1)
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/method', methods=['GET', 'POST'])      # 라우팅 주소를 가져오는 방식 설정
def login():
    if request.method == 'POST':
        return "Post"
    else:
        return "Get"

@app.route('/login')        # 기본 방식 : GET 방식, http://127.0.0.1:8089/login?name=lee
def login1():
    user = request.args.get('username')
    return 'User %s' %user

@app.route('/login', methods=['POST'])        # POST 방식(방식이 하나일 때도 리스트 형식으로)
def login2():
    # if request.method == 'POST':
    uname = request.form['username']
    pw = request.form['password']
    return 'Username : %s, Password : %s' %(uname, pw)

if __name__ == '__main__':
    app.run(debug=True,port=8089)