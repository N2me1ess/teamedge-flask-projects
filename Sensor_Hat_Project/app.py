from flask import Flask,render_template, redirect, url_for, request
app = Flask(__name__)

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
   if request.method == 'POST':
      user = request.form['tx']
      return redirect(url_for('text_sent',text = user))
   else:
      user = request.args.get('tx')
      return redirect(url_for('text_sent',text = user))

@app.route("/text_sent/<text>")
def text_sent(text): # Text variable needs to be send to raspimon, 
    return render_template("text_sent")

if __name__ == '__main__':
   app.run(debug = True)