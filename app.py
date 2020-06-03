from flask import Flask,render_template,flash,redirect,url_for,session,logging,request,Response
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime





app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Contact(db.Model):
    __tablename__ = 'Contact'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    name = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    subject = db.Column(db.String(150))
    message= db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def __init__(self,name,mail,subject,message):
        self.name=name
        self.mail=mail
        self.subject=subject
        self.message=message
       
        

       
    
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/index', methods=['GET','POST'])
def Register():

     if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        reg = Contact(name = name,mail = email, subject = subject,message= message)
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('index'))




if(__name__ == "__main__"):
    app.run(debug=True)
