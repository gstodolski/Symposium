import os
import datetime

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date, datetime

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///symposium.db")

@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    if request.method == "GET":
        courses = db.execute("SELECT * FROM user_courses INNER JOIN courses ON user_courses.course_id=courses.course_id WHERE user_id=:user_id ORDER BY subject", user_id= session["user_id"])
        return render_template("index.html", courses=courses)

    else:
        course_id = request.form['button']
        return redirect(url_for('course', course_id=course_id))

@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 403)
        # Ensure password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password and confirmation must match", 403)

        check= db.execute("SELECT username FROM users where username= :username", username=request.form.get("username"))
        if not check:
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                        username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))
            return redirect("/")
        else:
            return apology("This username already exists", 403)
        # Redirect user to home page


    else:
        return render_template("register.html")

@app.route("/search", methods=["GET", "POST"])
@login_required
def search():

    if request.method == "GET":
        return render_template("search.html")
        #return render_template("searched.html")

    else:
        subject = request.form.get("subject")
        number = request.form.get("number")
        name = request.form.get("name")

        if not name and not number:
            return apology("Please enter a name or number", 403)
        elif not subject:
            return apology("Please choose a subject")
        elif not number:
            course = db.execute("SELECT * FROM courses WHERE name=:name", name=name)
        elif not name:
            course = db.execute("SELECT * FROM courses WHERE subject=:subject AND number=:number", subject=subject, number=number)
        elif not course:
            return apology("Course not found", 403)

        return render_template("searched.html", course= course)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():

    if request.method == "POST":
        semester = request.form.get("semester")
        name = request.form.get("name")
        number = request.form.get("number")
        subject = request.form.get("subject")

        course_db = db.execute("SELECT * FROM courses WHERE subject= :subject AND number= :number", subject=subject, number=number)
        if not course_db:
            course_db = db.execute("SELECT * FROM courses WHERE name=:name", name=name)
        if len(course_db) < 1:
            return apology("We could not find this course", 404)
        course_id=int(course_db[0]["course_id"])

        """if not name and not number:
            return apology("Please enter a name or number", 403)
        elif not number:
            course_db = db.execute("SELECT * FROM courses WHERE subject= :subject AND name= :name", subject=subject, name=name)
        elif not name:
            course_db=db.execute("SELECT * FROM courses WHERE subject= :subject AND number= :number", subject=subject, number=number)
        elif not semester:
            return apology("Please enter a semester", 403)
        elif not subject:
            return apology("Please choose a subject")
        elif not number:
            course = db.execute("SELECT * FROM courses WHERE name=:name", name=name)
        elif not name:
            course = db.execute("SELECT * FROM courses WHERE subject=:subject AND number=:number", subject=subject, number=number)
        elif len(course_db) < 1:
            return apology("We could not find this course", 404)"""

        #Check if already addeds
        check = db.execute("SELECT * FROM user_courses INNER JOIN courses ON user_courses.course_id=courses.course_id WHERE name=:name AND user_id=:user_id", name=course_db[0]["name"], user_id= session["user_id"])
        if not check:
            db.execute("INSERT INTO user_courses(user_id, course_id, semester) VALUES(:user_id, :course_id, :semester)", user_id=session["user_id"], course_id=course_id, semester=semester)
        else:
            return apology('You have already added this course', 403)
        return redirect("/")

    else:
        return render_template("add.html")

@app.route("/remove", methods=["GET", "POST"])
@login_required
def remove():

    if request.method == "POST":
        name = request.form.get("name")
        number = request.form.get("number")
        subject = request.form.get("subject")

        course_db = db.execute("SELECT * FROM courses WHERE subject= :subject AND number= :number", subject=subject, number=number)
        if not course_db:
            course_db = db.execute("SELECT * FROM courses WHERE name=:name", name=name)
        if len(course_db) < 1:
            return apology("We could not find this course", 404)
        course_id=int(course_db[0]["course_id"])

        #Check
        check = db.execute("SELECT * FROM user_courses INNER JOIN courses ON user_courses.course_id=courses.course_id WHERE subject = :subject AND number = :number AND user_id = :user_id", subject=subject, number=number, user_id=session["user_id"])
        if check:
            db.execute("DELETE FROM user_courses WHERE course_id=:course_id AND user_id=:user_id", course_id=course_id, user_id=session["user_id"])
        else:
            return apology("We could not find this course", 403)

        return redirect("/")

    else:
        return render_template("remove.html")

@app.route("/course", methods=["GET", "POST"])
@login_required
def course():

    if request.method == "POST":
        post = request.form.get('text')
        if not post:
            return apology("please input text for your post", 403)
        today = date.today()
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        course_id = (request.args.get('course_id'))#['course_id']
        #course_id= int(course)
        db.execute("INSERT INTO posts VALUES (:user_id, :course_id, :post, :date, :time)",
                    user_id=session["user_id"], course_id=course_id, post=post, date=today, time=time)

        #course = db.execute("SELECT * FROM courses WHERE course_id=:course_id", course_id=course_id)
        #posts = db.execute("SELECT * FROM posts INNER JOIN users ON posts.user_id=users.id WHERE course_id=:course_id", course_id=course_id)
        #subject = str(course[0]['subject'])
        #number = str(course[0]['number'])
        #name = str(course[0]['name'])

        return redirect(url_for('course', course_id=course_id))
        #return render_template("course.html", subject=subject, number=number, name=name, posts=posts)
    else:
        #course = db.execute("SELECT * FROM courses WHERE ")
        course_id = request.args['course_id']
        course = db.execute("SELECT * FROM courses WHERE course_id=:course_id", course_id=course_id)
        posts = db.execute("SELECT * FROM posts INNER JOIN users ON posts.user_id=users.id WHERE course_id=:course_id", course_id=course_id)
        subject = str(course[0]['subject'])
        number = str(course[0]['number'])
        name = str(course[0]['name'])

        return render_template("course.html", subject=subject, number=number, name=name, posts=posts, course_id=course_id)