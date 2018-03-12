from flask import Flask, render_template, request
app = Flask(__name__)

import tradeinspace.createdb
import tradeinspace.planetlist

@app.route("/")
def index():
	worlds = planetlist.planetList()
	return render_template("index.html", worldsList = worlds)

@app.route("/createuniverse.html", methods=["GET", "POST"])
def createUniverse():
	if request.method == "POST":
		createdb.createWorld()
		return render_template("universecreated.html")
	else:
		return render_template("createuniverse.html")
