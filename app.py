from flask import Flask,request,redirect,render_template,session, flash
import sessions

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if "uid" in session:
        return redirect("/")

    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        pass
        # log the user in

@app.route('/register',methods=['GET','POST'])
def register():
    if "uid" in session:
        return redirect("/")

    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        pass
        # register the user

@app.route("/account", methods=["GET", "POST"])
def account():
    if not "uid" in session:
        return redirect ("/")

    if request.method == "GET":
        return render_template("account.html")
    if request.method == "POST":
        pass
        # update password


@app.route('/schedule')
def schedule():
    if "uid" in session:
        return redirect("/")

    if request.method == "GET":
        # fetch current schedule
        return render_template("schedule.html")
    if request.method == "POST":
        pass
        # update schedule

if __name__== "__main__":
    app.run()
