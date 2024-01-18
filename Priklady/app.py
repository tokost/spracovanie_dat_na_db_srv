# app.py

# import Flask and render_template
from flask import Flask, render_template

# import sqlite3 library for database connection
import sqlite3

# create a Flask instance called app
app = Flask(__name__)

# route the default URL


@app.route("/")
def home():
    # connect to the example.db database
    conn = sqlite3.connect("example.db")
    # create a cursor object to execute SQL commands
    c = conn.cursor()
    # execute a SQL command
    c.execute("SELECT * FROM users")
    # retrieve all the data from the users table
    users = c.fetchall()
    # close the database connection
    conn.close()
    # render the index.html template
    return render_template("index.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
