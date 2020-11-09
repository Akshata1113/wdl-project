
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy


import urllib.request
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/wee'
db = SQLAlchemy(app)
class Index(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String,  nullable=False)
    lname = db.Column(db.String(80),  nullable=False)
    bName = db.Column(db.String(120),  nullable=False)
    email = db.Column(db.String, nullable=False)
    paddress = db.Column(db.String(80),  nullable=False)
    dropaddress= db.Column(db.String(6), nullable=False)
    sdate = db.Column(db.String(6), nullable=False)
    edate = db.Column(db.String,  nullable=False)
    state = db.Column(db.String(120),  nullable=False)
    ncard = db.Column(db.Integer,  nullable=False)
    ccno = db.Column(db.String(80),  nullable=False)
    expiration = db.Column(db.String(6),  nullable=False)
    cvv = db.Column(db.String(120),  nullable=False)

class Contacts(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),  nullable=False)
    phone=db.Column(db.String(12),  nullable=False)
    email=db.Column(db.String(20),  nullable=False)
    msg=db.Column(db.String(120), nullable=False)
@app.route('/')
@app.route('/index.html',methods=['GET','POST'])
def helloworld():

    if(request.method=='POST'):
        Firstname =request.form.get('fname')
        Lastname = request.form.get('lname')
        BikeName = request.form.get('bname')
        Email = request.form.get('email')
        PickupAddress= request.form.get('paddress')
        DropAddress = request.form.get('daddress')
        StartDate = request.form.get('sdate')
        EndDate = request.form.get('edate')
        State = request.form.get('state')
        Nameoncard = request.form.get('ncard')
        Creditcardnumber = request.form.get('ccno')
        Expiration = request.form.get('expiration')
        CVV = request.form.get('cvv')
        entry=index(fname=firstname,lname=Lastname,bname=BikeName,paddress=PickupAddress,daddress=DropAddress,
                      sdate=startdate,edate=enddate,ncard=cc-name,ccno=Credircardnumber,expiration=Expiration,cvv=CVV)
        db.session.add(entry)
        db.session.commit()

    return render_template('index.html')





@app.route('/')
def BikeHome():
    return render_template('BikeHome.html')


@app.route('/marketplace.html')
def marketplace():
    return render_template('marketplace.html')

@app.route('/whywee.html')
def whywee():
    return render_template('whywee.html')

@app.route('/contact.html',methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        phone=request.form.get('phone')
        email=request.form.get('email')
        message=request.form.get('message')

        entry=Contacts(name=name,phone=phone,email=email,msg=message)
        db.session.add(entry)
        db.session.commit()



    return render_template('contact.html')





@app.route('/login.html')
def upload_form():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)








#app.run(debug=True)
