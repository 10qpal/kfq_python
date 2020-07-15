from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' %session['username']
    return 'You are not logged in'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']      # post 방식 : form으로 받는다
        return redirect('/')
        # return redirect(url_for('index'))
    # render_template('html 주소')로 호출해도 되지만 간단하니까
    return '''
    <form action="" method="post">
    <p><input type="text" name="username"/>
    <p><input type="submit" value="login"/>
    </form>
    ''' 

# 세션 사용 위해서는 시크릿키 필요(시크릿키는 아무거나)
app.secret_key = 'h09r23hfg0j1f'

@app.route('/logout')
def logout():
    session.pop('username', None)       # 세션 : 딕셔너리 형태
    return redirect('/')

if __name__ == '__main__':
    app.run()