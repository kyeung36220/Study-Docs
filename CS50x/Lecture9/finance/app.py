import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    portfolio_exists = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='portfolio';")
    if portfolio_exists:
        user_exists = db.execute("SELECT name FROM portfolio WHERE user = ?", session["user_id"])

    if portfolio_exists and user_exists:
        portfolio = db.execute("SELECT * FROM portfolio WHERE user = ?", session["user_id"])
        cash = round(db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash'], 2)
        grand_total = cash
        for stock in portfolio:
            current_price = round(float(lookup(stock['symbol'])['price']), 2)
            db.execute("UPDATE portfolio SET current_price = ? WHERE symbol = ?", current_price, stock['symbol']) #update current price
            db.execute("UPDATE portfolio SET total_value = ? WHERE symbol = ?", round(current_price * stock['quantity'], 2), stock['symbol']) #update total value
            grand_total += stock["total_value"]

    else:
        grand_total = 0
        portfolio = []
        cash = 0

    return render_template("index.html", user=session["user_id"], portfolio=portfolio, portfolio_exists=portfolio_exists, cash=usd(cash), grand_total=usd(grand_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").lower()
        quantity = request.form.get("shares")

        if quantity.isnumeric() == False or float(quantity) <= 0:
            return apology("INVALID QUANTITY")
        else:
            try:
                quantity = int(quantity)
            except ValueError:
                return apology("INVALID QUANTITY")
        try:
            info = lookup(symbol)
            name, price, symbol = info['name'], info['price'], info['symbol']
        except TypeError: #if lookup doesn't find stock
            return apology("STOCK NOT FOUND")

        print(db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"]))
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash'] #returns dictionary so I need to specify
        if user_cash < float(price) * quantity: #if not enough money
            return apology("NOT ENOUGH CASH")

        portfolio_exists = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='portfolio';") #checking if portfolio table exists
        if not portfolio_exists:
            db.execute("CREATE TABLE portfolio (name TEXT NOT NULL, symbol TEXT NOT NULL, quantity INTEGER NOT NULL, current_price NUMERIC NOT NULL, total_value NUMERIC NOT NULL, user INTEGER NOT NULL)")

        in_portfolio = db.execute("SELECT name from portfolio WHERE symbol = (?) AND user = (?)", symbol, session["user_id"]) #checking if stock exists in portfolio
        if not in_portfolio:
            db.execute("INSERT INTO portfolio (name, symbol, quantity, current_price, total_value, user) VALUES(?, ?, ?, ?, ?, ?)",name, symbol, quantity, price, price * quantity, session["user_id"])
        else:
            added_quantity = int(db.execute("SELECT quantity FROM portfolio WHERE symbol = ? AND user = ?", symbol, session["user_id"])[0]['quantity'] + quantity)
            db.execute("UPDATE portfolio SET quantity = ? WHERE symbol = ?", added_quantity, symbol)

        db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash - (int(price) * quantity), session["user_id"]) #subtracting money

        history_exists = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='history';") #checking if history table exists
        if not history_exists:
            db.execute("CREATE TABLE history (bought_or_sold TEXT NOT NULL, symbol TEXT NOT NULL, price NUMERIC NOT NULL, quantity INTEGER NOT NULL, date, time, user INTEGER NOT NULL)")
        date = db.execute("SELECT strftime('%Y-%m-%d', 'now')")[0]['strftime(\'%Y-%m-%d\', \'now\')']
        time = db.execute("SELECT strftime('%H:%M:%S', 'now')")[0]['strftime(\'%H:%M:%S\', \'now\')']
        db.execute("INSERT INTO history (bought_or_sold, symbol, price, quantity, date, time, user) VALUES(?, ?, ?, ?, ?, ?, ?)", 'Bought', symbol, (int(price) * quantity), quantity, date, time, session["user_id"])

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    #Display table with history of all transactions, listing one row for every buy and sell (INfo on what stock, how many shares, and when)
    """Show history of transactions"""
    history_exists = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='history';") #checking if history table exists
    if history_exists:
        history = db.execute("SELECT * FROM history WHERE user = ?", session["user_id"])
    else:
        history = []

    return render_template("history.html", history_exists = history_exists, history = history)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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
    """Get stock quote."""
    if request.method == "POST":
        try:
            info = lookup(request.form.get("symbol"))
            name, price, symbol = info['name'], info['price'], info['symbol']
            return render_template("quoted.html", name=name, price=usd(price), symbol=symbol)
        except TypeError:
            return apology("STOCK NOT FOUND")
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("EMPTY USERNAME")
        elif not password:
            return apology("EMPTY PASSWORD")
        elif not confirmation:
            return apology("EMPTY CONFIRMATION")
        elif password != confirmation:
            return apology("PASSWORD DON'T MATCH")
        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))
            rows = db.execute("SELECT * FROM users WHERE username = ?", username)
            session["user_id"] = rows[0]["id"]
        except ValueError:
            return apology("USERNAME ALREADY EXISTS")

        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    #POST: check for possible errors and sell number of shares and update user's cash (actually has number of sahres or can't sell negative)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quantity = int(request.form.get("shares"))

        if quantity <= 0:
            return apology("CANNOT ENTER QUANTITY LESS THAN OR EQUAL TO THAN 0")
        try:
            info = lookup(symbol)
            price, symbol = info['price'], info['symbol']
        except TypeError: #if lookup doesn't find stock
            return apology("STOCK NOT FOUND")
        try:
            portfolio_stock = db.execute("SELECT * FROM portfolio WHERE symbol = ?", symbol)[0]
        except KeyError:
            return apology("STOCK NOT IN PORTFOLIO")
        if portfolio_stock['quantity'] < quantity:
            return apology("NOT ENOUGH QUANTITY IN PORTFOLIO")

        db.execute("UPDATE portfolio SET quantity = ? WHERE symbol = ?", portfolio_stock['quantity'] - quantity, symbol)
        current_cash = round(db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash'] , 2)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", ((portfolio_stock['quantity'] - quantity) * price) + current_cash, session["user_id"])

        date = db.execute("SELECT strftime('%Y-%m-%d', 'now')")[0]['strftime(\'%Y-%m-%d\', \'now\')']
        time = db.execute("SELECT strftime('%H:%M:%S', 'now')")[0]['strftime(\'%H:%M:%S\', \'now\')']
        db.execute("INSERT INTO history (bought_or_sold, symbol, price, quantity, date, time, user) VALUES(?, ?, ?, ?, ?, ?, ?)", 'Sold', symbol, (int(price) * quantity), quantity, date, time, session["user_id"])

        return redirect("/")

    else:
        return render_template("sell.html")

@app.route("/adjust", methods=["GET", "POST"])
@login_required
def adjust():
    """Sell shares of stock"""
    if request.method == "POST":
        amount = request.form.get("cash")
        action = request.form.get("action")
        number_checker = r'^\d+(\.\d{1,2})?$'
        current_balance = round(db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash'] , 2)

        if not re.match(number_checker, amount):
            return apology("INVALID AMOUNT")
        elif float(amount) <= 0:
            return apology("AMOUNT MUST BE A POSTIVE INTEGER")
        elif action == "withdraw" and float(amount) >= current_balance:
            return apology("NOT ENOUGH MONEY")


        if action == "add":
            db.execute("UPDATE users SET cash = ? WHERE id = ?", current_balance + float(amount), session["user_id"])
        elif action == "withdraw":
            db.execute("UPDATE users SET cash = ? WHERE id = ?", current_balance - float(amount), session["user_id"])

        return redirect("/")
    else:
        return render_template("adjust.html")
