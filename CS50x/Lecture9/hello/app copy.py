#from flask import Flask, render_template, request

#app = Flask(__name__)

#@app.route("/")
#def index():
    #name = request.args.get("name", "world") first argument is get a key second argument is when none
    #return render_template("index.html")

#@app.route("/greet", methods=["POST"]) #post is more private than get
#def greet():
    #name = request.form.get("name", "world") #request.args works with get and form works with post
    #return render_template("greet.html", name=name)
