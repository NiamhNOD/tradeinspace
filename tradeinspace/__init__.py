from flask import Flask, render_template, request
app = Flask(__name__)

import tradeinspace.createdb

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/createuniverse.html", methods=["GET", "POST"])
def createUniverse():
	if request.method == "POST":
		createdb.createWorld()
		return render_template("universecreated.html")
	else:
		return render_template("createuniverse.html")
