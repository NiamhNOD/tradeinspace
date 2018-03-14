from tradeinspace import app
from tradeinspace import Player
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import uuid

# setup the postgres database location
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/tradeinspace"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# open the connection to the database
db = SQLAlchemy(app)

# connect Bcrypt
bycrypt_app = Bcrypt(app)

def check_password(username, password):
    user = User.query.filter(playername=username).first()
    hashedpassword = user.playerpassword
    salt = user.playersalt
    passwordtocheck = password + salt
    return bycrypt_app.check_password_hash(hashedpassword, passwordtocheck)
