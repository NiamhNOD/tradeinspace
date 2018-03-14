from tradeinspace import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import random
import uuid

# setup the postgres database location
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/tradeinspace"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# open the connection to the database
db = SQLAlchemy(app)

# connect Bcrypt
bycrypt_app = Bcrypt(app)

# create the class for the player
class Player(db.Model):
	playerid = db.Column(db.Integer, primary_key=True)
	playername = db.Column(db.String(80), unique=True, nullable=False)
	playerpassword = db.Column(db.String, nullable=False)
	playersalt = db.Column(db.String)

# create the class for world names
class World(db.Model):
	worldid = db.Column(db.Integer, primary_key=True)
	worldname = db.Column(db.String(80), unique=True, nullable=False)

# create the class for product details
class Products(db.Model):
	productid = db.Column(db.Integer, primary_key=True)
	product = db.Column(db.String(80), unique=True)
	size = db.Column(db.Float)
	sizedescriptor = db.Column(db.String(80))
	baseprice = db.Column(db.Integer)

# create the class for the individual products in each world
class WorldPrices(db.Model):
	worldproductsid = db.Column(db.Integer, primary_key=True)
	worldid = db.Column(db.Integer, db.ForeignKey('world.worldid'))
	productsid = db.Column(db.Integer, db.ForeignKey('products.productid'))
	price = db.Column(db.Integer)
	amount = db.Column(db.Integer)

# create the database
def createWorld():
	db.drop_all()
	# create the database tables
	db.create_all()

	# put each world into the worlds table
	worlds = ['Ireland', 'England', 'Scotland', 'Wales', 'France', 'Italy']
	for x in worlds:
		world = World(worldname = x)
		db.session.add(world)
	db.session.commit()

	# put each product into the products table
	productList = [['water', 1, 'l', 100], ['clay', 1, 'kg', 50], ['iron', 1, 'kg', 160], ['gold', 0.001, 'gm', 3000],
					['Copper', 1, 'kg', 600], ['Silver', 0.01, 'gm', 600]]
	for x in range(len(productList)):
		product = Products(product = productList[x][0], size = productList[x][1], sizedescriptor = productList[x][2],
					baseprice = productList[x][3])
		db.session.add(product)
	db.session.commit()

	# create each worlds price for an individual product
	for x in range(len(worlds)):
		for y in range(len(productList)):
			price = int(productList[y][3] * random.uniform(0.75, 1.25))
			amount = random.randrange(50, 150)
			priceentry = WorldPrices(worldid = x + 1, productsid = y + 1, price = price, amount = amount)
			db.session.add(priceentry)
	db.session.commit()

	# create the default user
	playeruuid = str(uuid.uuid4())
	playerpasswordraw = str(12345678)
	playerasswordsalt = playerpasswordraw + playeruuid
	playerpassword = bcrypt_app.generate_password_hash(playerpasswordsalt)
	user = Player(playername = Admin, playerpassword = playerpassword 12345678, playersalt = playeruuid)
	db.session.add(user)
	db.session.commit()
