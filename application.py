import os
import datetime

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

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

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


# Help from Hainan at Benedict's OH 11/21
@app.route("/")
@login_required
def index():
    stocks = db.execute("SELECT *, SUM(shares), SUM(total) FROM stocks WHERE user_id=:user_id GROUP BY symbol", user_id=session["user_id"])
    return render_template("index.html", stocks=stocks, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology ("must include symbol", "403")
        elif not request.form.get("shares"):
            return apology ("must include number of shares", "403")

        stonk = lookup(request.form.get("symbol"))
        if not stonk:
            return apology("Invalid symbol", 403)
        cost = float(request.form.get("shares")) * float(stonk["price"])
        cash = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])
        timestamp = datetime.datetime.now()
        if cost > cash[0]["cash"]:
            return apology("you're broke")
        else:
            cash[0]["cash"] = cash[0]["cash"] - cost
            db.execute("UPDATE users SET cash=:cash WHERE id=:user_id", cash=cash[0]["cash"], user_id=session["user_id"])
            db.execute("INSERT INTO stocks VALUES (:user_id, :symbol, :name, :price, :shares, :total, :timestamp)",
                            user_id=session["user_id"], symbol=stonk["symbol"], name=stonk["name"],
                            price=stonk["price"], shares=request.form.get("shares"), total=cost, timestamp=timestamp)
            db.execute("INSERT INTO history VALUES (:user_id, :symbol, :name, :price, :shares, :total, :timestamp)",
                            user_id=session["user_id"], symbol=stonk["symbol"], name=stonk["name"],
                            price=stonk["price"], shares=request.form.get("shares"), total=cost, timestamp=timestamp)
            return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    stocks = db.execute("SELECT * FROM history WHERE user_id=:user_id ORDER BY timestamp DESC", user_id=session["user_id"])
    return render_template("history.html", stocks=stocks)

@app.route("/shop", methods=["GET", "POST"])
@login_required
def shop():
    if request.method == "POST":
        cash = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])
        cash[0]["cash"] = cash[0]["cash"] + 1000
        db.execute("UPDATE users SET cash=:cash WHERE id=:user_id", cash=cash[0]["cash"], user_id=session["user_id"])
        return redirect("/")

    else:
        return render_template("shop.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    if request.method == "POST":
        stonk = lookup(request.form.get("symbol"))
        if request.form.get("symbol") == "MEME":
            return redirect("https://i.kym-cdn.com/photos/images/newsfeed/001/499/826/2f0.png")
        elif not stonk:
            return apology("Invalid symbol", 403)
        return render_template("quoteresponse.html", stonk=stonk)
    else:
        return render_template("quote.html")


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

        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                    username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology ("must include symbol", "403")
        elif not request.form.get("shares"):
            return apology ("must include number of shares", "403")
        numberofstocks = db.execute("SELECT *, SUM(shares) FROM stocks WHERE symbol=:symbol AND user_id=:user_id GROUP BY symbol",
                                        symbol=request.form.get("symbol"), user_id=session["user_id"])
        if not numberofstocks:
            return apology ("must have this stock", "403")

        sale = lookup(request.form.get("symbol"))
        cost = float(request.form.get("shares")) * float(sale["price"])
        cash = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])
        timestamp = datetime.datetime.now()
        stocks = db.execute("SELECT *, SUM(shares) FROM stocks WHERE symbol=:symbol GROUP BY symbol", symbol=request.form.get("symbol"))
        if int(stocks[0]["SUM(shares)"]) < int(request.form.get("shares")):
            return apology("you don't have that many stocks", "403")
        else:
            cash[0]["cash"] = cash[0]["cash"] + cost
            shareloss = int(request.form.get("shares")) * -1
            print(shareloss)
            db.execute("UPDATE users SET cash=:cash WHERE id=:user_id", cash=cash[0]["cash"], user_id=session["user_id"])
            db.execute("INSERT INTO stocks VALUES (:user_id, :symbol, :name, :price, :shares, :total, :timestamp)",
                        user_id=session["user_id"], symbol=sale["symbol"], name=sale["name"], price=sale["price"],
                        shares=shareloss, total=(sale["price"]*shareloss), timestamp=timestamp)
            db.execute("INSERT INTO history VALUES (:user_id, :symbol, :name, :price, :shares, :total, :timestamp)",
                        user_id=session["user_id"], symbol=sale["symbol"], name=sale["name"], price=sale["price"],
                        shares=shareloss, total=(sale["price"]*shareloss), timestamp=timestamp)
            if (shareloss + stocks[0]["SUM(shares)"]) == 0:
                print("0")
                db.execute("DELETE FROM stocks WHERE symbol=:symbol", symbol=request.form.get("symbol"))
            return redirect("/")

    else:
        stocks = db.execute("SELECT *, SUM(shares) FROM stocks WHERE user_id=:user_id GROUP BY symbol", user_id=session["user_id"])
        return render_template("sell.html", stocks=stocks)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
