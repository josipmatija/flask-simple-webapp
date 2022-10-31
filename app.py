from flask import Flask, render_template, request

#the following line means "hey python, turn this file into flask application"
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#we added POST method because flask by default supports GET only, we need POST so our input is not visible in the URL
@app.route("/greet", methods=["POST"])
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name=name)
