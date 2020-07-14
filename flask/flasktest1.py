# (1)
# from flask import Flask
# app = Flask(__name__)       # 플라스크 개체 생성
# @app.route('/')     # 요청에 대한 처리
# def index():
#     return 'Hello World'

# if __name__ == '__main__':      # 실행 조건
#     app.run()       # 웹 애플리케이션 실행

# (2)
# from flask import Flask, render_template      # template에서 html 불러오기 위해
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()

# (3)
# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')     # http://127.0.0.1:5000/
# def index():
#     return render_template('index.html')

# @app.route('/cakes')        # http://127.0.0.1:5000/cakes
# def cakes():
#     return "Yammy cakes!"

# if __name__ == '__main__':
#     app.run()

# (4)
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')     # http://127.0.0.1:5000/
def index():
    return render_template('index.html')

@app.route('/cakes')        # http://127.0.0.1:5000/cakes
def cakes():
    return "Yammy cakes!"

@app.route('/user/<username>')      # 이런 형식인 경우에(http://127.0.0.1:5000/user/lee)
def show_user_profile(username):        # 처리하는 함수 안에 인자 전달해야
    return 'User %s' %username

@app.route('/user/<username>/<int:age>')        # http://127.0.0.1:5000/user/lee/25
def show_user_profile_age(username,age):
    return 'Username %s, Age %d' %(username,age)

if __name__ == '__main__':      # 자기 파일에서 호출할 경우에만 __name__ = __main__
    app.run()                   # 다른 함수에서 호출할 경우에는 __name__ = 파일 이름이 된다