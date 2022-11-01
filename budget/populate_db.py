"""
populate_db.py
--------------

Populate the DB.

"""

import sqlite3
from datetime import datetime


def to_date(date_str):
    return datetime.strptime(date_str, "%d.%m.%y")


data = [
    (to_date("29.10.22"), 25, "Daily budget"),
    (to_date("29.10.22"), -40, "Rewe"),
    (to_date("29.10.22"), -17, "DM"),
    (to_date("30.10.22"), 25, "Daily budget"),
    (to_date("31.10.22"), 25, "Daily budget"),
    (to_date("01.11.22"), -13, "Aspendos Doner"),
    (to_date("01.11.22"), -30, "DM"),
    (to_date("01.11.22"), -25, "Rewe"),
    (to_date("01.11.22"), 25, "Daily budget"),
]


def main():
    """Mess around with sqlite."""
    con = sqlite3.connect("budget/budget.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE transactions(stamp, amount, store)")
    cur.executemany("INSERT INTO transactions VALUES(?, ?, ?)", data)
    con.commit()

    con.close()


if __name__ == "__main__":
    main()
