"""
app.py
------

Flask app serving from the sqlite DB.

"""

from flask import Flask, request, render_template
from datetime import datetime
import sqlite3


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = request.form["amount"]
        store = request.form["store"]
        commit_transaction(datetime.now(), -int(amount), store)
    with sqlite3.connect("budget/budget.db") as con:
        cur = con.cursor()
        res = cur.execute("SELECT sum(amount) FROM transactions")
    balance = res.fetchall()[0][0]
    return render_template("index.html", balance=balance)


def commit_transaction(stamp, amount, store):
    cmd = "INSERT INTO transactions VALUES(?, ?, ?)"
    with sqlite3.connect("budget/budget.db") as con:
        cur = con.cursor()
        res = cur.execute(cmd, (stamp, amount, store))
        con.commit()
