from flask import Flask,render_template, redirect, url_for, request
from flask_apscheduler import APScheduler
from sense_hat import SenseHat 
import sqlite3

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route("/")
def home_page():
    return render_template("home_page.html")

@app.route("/add")
def add_page():
    return render_template("add_page.html")

@app.route("/delete")
def delete_page():
    return render_template("delete_page.html")



if __name__ == '__main__':
   app.run(debug = True)