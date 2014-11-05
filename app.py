from flask import Flask,request,redirect,render_template,session
import db

app=Flask(__name__)

@app.route('/')
def home():
    return redirect('home')

@app.route('/login',methods=['GET','POST'])
def login():

@app.route('/register',methods=['GET','POST'])
def register():

@app.route('/schedule')
def schedule():

@app.route('/archive')
def archive():
         
