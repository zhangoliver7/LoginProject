from flask import Flask,request,redirect,render_template,session
import sessions

app=Flask(__name__)

@app.route('/')
def home():
    session = MongoSessionInterface()
    #print session
    return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def login():
    pass

@app.route('/register',methods=['GET','POST'])
def register():
    pass

@app.route('/schedule')
def schedule():
    pass

@app.route('/archive')
def archive():
    pass
         
if __name__== "__main__":
    app.run()
