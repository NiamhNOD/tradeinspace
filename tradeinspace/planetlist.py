from tradeinspace.createdb import World
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tradeinspace import app

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/tradeinspace"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def planetList():
    worlds = World.query.order_by(World.worldname).all()
    return worlds
