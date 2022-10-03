from urllib import request
from flask import Flask, redirect, url_for, render_template,request
from flask_db2 import DB2

#Initialization and global variables
app = Flask(__name__)
db = DB2(app)

#Scheduler Part

#Wrapper Functions

#Routes
@app.route('/')
def home():
    return "Hi"

@app.route('/register',methods = ['POST', 'GET'])
def register():
    if request.method=='POST':
        return redirect(url_for('display',user = request.form['email']))
    return render_template("register.html")

@app.route('/display/<user>',methods=['POST','GET'])
def display(user):
    return "registered mail is "+user

#Main Function
if __name__=='__main__':
    app.run()