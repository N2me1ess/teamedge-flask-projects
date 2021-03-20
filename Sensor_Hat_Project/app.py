from flask import Flask,render_template, redirect, url_for, request
from sense_hat import SenseHat 
app = Flask(__name__)
sense = SenseHat()


@app.route("/")
def home_page():
    return render_template("name.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/success/<name>')
def success(name):
   return "<p> Welcome %s to Cristian's Sensorhat.</p> <p>Go to /text to have text displayed on your Sensor Hat. Or use /display to edit your raspimon </p>" % name  

# Break this so I dont get brain cancer

@app.route("/text") # Renders text html with /text
def text():
    return render_template("text.html")

@app.route('/text_recieved',methods = ['POST', 'GET']) # Goes to this site to do something with text
def text_recieved():
      text = request.form['text']
      sense.show_message(text)
      return render_template("text_sent.html", text = text)


if __name__ == '__main__':
   app.run(debug = True)