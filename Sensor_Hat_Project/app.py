from flask import Flask,render_template, redirect, url_for, request
from sense_hat import SenseHat 
import sqlite3
app = Flask(__name__)
sense = SenseHat()
name = "yikers"

@app.route("/")
def home_page():
    return render_template("name.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('text',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('text',name = user)) 

# Break this so I dont get brain cancer

@app.route("/text/<name>") # Renders text html with /text
def text(name):
   return render_template("text.html", name = name)

@app.route('/text_recieved',methods = ['POST']) # Goes to this site to do something with text
def text_recieved():
      message = request.form['text']
      conn = sqlite3.connect('./static/data/senseDisplay.db')
      curs = conn.cursor()
      curs.execute("INSERT INTO messages (name, message) VALUES((?), (?))",(name, message))

      conn.commit()
      conn.close()

      sense.show_message(message)
      return render_template("text_sent.html", message = message)


if __name__ == '__main__':
   app.run(debug = True)