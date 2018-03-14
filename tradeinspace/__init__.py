from flask import Flask, render_template, request
from flask.ext.login import LoginManager
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

import tradeinspace.createdb
import tradeinspace.planetlist
import tradeinspace.user

@login_manager.user_loader
def load_user(user_id):
	return User.get_id(user_id)

# return the index page with the link to the DB creation page and a link
# to the world list page
@app.route("/")
def index():
	worlds = planetlist.planetList()
	return render_template("index.html", worldsList = worlds)

@app.route("/login", methods=["GET", "POST"])
def login():
	if request = "POST":
		password = check_password()
		if password:
			return render_template("loggedin.html")
		else:
			return render_template("login.html")
	else:
		return render_template("login.html")

# return the create universe page to create the universe DB
@app.route("/createuniverse.html", methods=["GET", "POST"])
def createUniverse():
	if request.method == "POST":
		createdb.createWorld()
		return render_template("universecreated.html")
	else:
		return render_template("createuniverse.html")

# return a page with a list of planets available
@app.route('/planet.html')
def planet1():
	worlds = planetlist.planetList()
	return render_template("planet.html", worldsList = worlds)

# return a page with the selected planet's product list
@app.route('/planet/<planet>.html')
def planet(planet):
	prices = planetlist.planetPrice(planet)
	return render_template('planetprices.html', planet=planet, prices=prices)
