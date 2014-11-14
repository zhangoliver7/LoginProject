from flask import Flask,request,redirect,render_template,session, flash, url_for
import db

app = Flask(__name__)
app.secret_key = "I'm all about that bass"

def login_required(func):
    def inner():
        if "uid" in session:
            return func()
        else:
            return redirect("/")
    return inner

def cant_be_logged_in(func):
    def inner():
        if not "uid" in session:
            return func()
        else:
            return redirect("/")
    return inner

@app.route('/')
def home():
    #show collections
    #show users
    #coll = db.users
    users = db.list_users
    return render_template("index.html", list = users)
    
@app.route('/login',methods=['GET','POST'])
@cant_be_logged_in
def login():

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        uid = db.password_correct(request.form["password"], request.form["username"]) 
        if uid:
            session["uid"] = uid
            return redirect("/")
        else:
            flash("Wrong username-password combination.")
            return render_template("login.html")
        # log the user in

@app.route("/logout")
@cant_be_logged_in
def logout():
    session.clear()
    return redirect("/")

@app.route('/register',methods=['GET','POST'])
@cant_be_logged_in
def register():

    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]
        period_1 = request.form["period-1"]
        period_2 = request.form["period-2"]
        period_3 = request.form["period-3"]
        period_4 = request.form["period-4"]
        period_5 = request.form["period-5"]
        period_6 = request.form["period-6"]
        period_7 = request.form["period-7"]
        period_8 = request.form["period-8"]
        period_9 = request.form["period-9"]
        period_10 = request.form["period-10"]

        if db.username_taken(username):
            flash("Username " + username + " is already taken.")
            return render_template("register.html")

        if password != confirm_password:
            flash("Passwords don't match.")
            return render_template("register.html")

        new_uid = db.new_user(username, password, (period_1, period_2, period_3, period_4, period_5, period_6, period_7, period_8, period_9, period_10))
        session["uid"] = new_uid
        return redirect(url_for("user", id=new_uid))


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():

    if request.method == "GET":
        return render_template("account.html")

    if request.method == "POST":
        old_password = request.form["old-password"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]
        if password != confirm_password:
            flash("Passwords don't match.")
            return render_template("account.html")

        if not db.password_correct(old_password, uid=session["uid"]):
            flash("Wrong password.")
            return render_template("account.html")
        
        db.update_password(session["uid"], password)

@app.route("/schedule", methods=["GET", "POST"])
@login_required
def schedule():

    if request.method == "GET":
        # fetch current schedule
        return render_template("schedule.html")
    if request.method == "POST":
        period_1 = request.form["period-1"]
        period_2 = request.form["period-2"]
        period_3 = request.form["period-3"]
        period_4 = request.form["period-4"]
        period_5 = request.form["period-5"]
        period_6 = request.form["period-6"]
        period_7 = request.form["period-7"]
        period_8 = request.form["period-8"]
        period_9 = request.form["period-9"]
        period_10 = request.form["period-10"]
        db.update_schedule(session["uid"], (period_1, period_2, period_3, period_4, period_5, period_6, period_7, period_8, period_9, period_10));
        return redirect(url_for("user", id=session["uid"]))

@app.route("/u")
def user():
    #return render_template(
    return "<br>".join(db.show_schedule(session["uid"]))
    #return db.users.find()
    #return "USER SCHEDULE WILL BE DISPLAYED HERE"

if __name__== "__main__":
    app.debug = True
    app.run()
