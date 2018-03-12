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

@app.route('/planet.html')
def planet1():
	worlds = planetlist.planetList()
	return render_template("planet.html", worldsList = worlds)

@app.route('/planet/<planet>.html')
def planet(planet):
	prices = planetlist.planetPrice(planet)
	return render_template('planetprices.html', planet=planet, prices=prices)
