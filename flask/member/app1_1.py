from flask import Flask,request,render_template,redirect,url_for,jsonify,json
import pymysql,os,cx_Oracle
from flask_sqlalchemy import SQLAlchemy
from json import JSONEncoder

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "oracle://hr:hr@127.0.0.1:1521/xe"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwer1234@localhost/test"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    #id =  db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.String(20),primary_key = True)
    userpw = db.Column(db.String(20))
    username = db.Column(db.String(20))
    userage = db.Column(db.Integer)
    usermail = db.Column(db.String(20))
    useradd = db.Column(db.String(20))
    usergender = db.Column(db.String(20))
    usertel = db.Column(db.String(20))

    def __repr__(self):
        return '<userid %r,username %r>' % (self.id,self.username)

    def __init__(self,userid,userpw,username,userage,usermail,useradd,usergender,usertel):
        self.userid=userid
        self.userpw=userpw
        self.username=username
        self.userage=userage
        self.usermail=usermail
        self.useradd=useradd
        self.usergender=usergender
        self.usertel=usertel

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usersform',methods=['POST','GET'])
def usersform():
    if request.method == 'GET':
        return render_template('usersform.html')   
    else:
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        username = request.form.get('username')
        userage = request.form.get('userage')
        usermail = request.form.get('useremail')
        useradd = request.form.get('useradd')
        usergender = request.form.get('usergender')
        usertel = request.form.get('usertel')
    
        my_user=User(userid,userpw,username,userage,usermail,useradd,usergender,usertel)       
        db.session.add(my_user)              
        db.session.commit()

    return redirect('/list')


@app.route('/list')
def list():
    all_data=User.query.all()
    return render_template('list.html',list=all_data)      

@app.route('/content/<userid>')
def content(userid):
    result=User.query.filter_by(userid = userid).one()
    return render_template('content.html',list=result)

@app.route('/updateform/<userid>',methods=['GET'])
def updateformget(userid):
    result=User.query.filter_by(userid = userid).one()
    return render_template('updateform.html',list=result)  

@app.route('/updateform',methods=['POST'])
def updateformpost():
    my_user = User.query.get(request.form.get('userid'))   
    
    my_user.userid = request.form.get('userid')
    my_user.userpw = request.form.get('userpw')
    my_user.username = request.form.get('username')
    my_user.userage = request.form.get('userage')
    my_user.usermail = request.form.get('usermail')
    my_user.useradd = request.form.get('useradd')
    my_user.usergender = request.form.get('usergender')
    my_user.usertel = request.form.get('usertel')  

    db.session.commit()

    return redirect('/list')    

@app.route('/deleteform/<userid>')
def deleteformget(userid):
    my_data = User.query.get(userid)
    db.session.delete(my_data)
    db.session.commit()
    return redirect('/list')  

@app.route('/ajaxlist',methods=['GET'])
def ajaxlistget():
    all_data=User.query.all()
    return render_template('ajaxlist.html',list=all_data)      

@app.route('/ajaxlist',methods=['POST'])
def ajaxlistpost():
    userid = request.form.get('userid')
    query = User.query.filter(User.userid.like('%'+userid+'%')). order_by(User.userid)
    all_data = query.all()
    print(all_data.toJSON())
    #return jsonify(all_data)
    return all_data.toJSON()       

@app.route('/imglist')
def imglist():
    print(os.path.dirname(__file__))
    dirname=os.path.dirname(__file__) + '/static/img/'
    filenames = os.listdir(dirname)
    print(filenames)
    return render_template('imglist.html',filenames=filenames)        

if __name__ =='__main__':
    db.create_all()
    app.run(debug=True,host='127.0.0.1',port=8890)