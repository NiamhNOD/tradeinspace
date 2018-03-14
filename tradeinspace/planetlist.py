from tradeinspace.createdb import World, WorldPrices, Products
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tradeinspace import app

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/tradeinspace"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def planetList():
    worlds = World.query.order_by(World.worldname).all()
    return worlds

def planetPrice(worldname):
    world = World.query.filter_by(worldname=worldname).first()
    worldid = str(world.worldid)
    return WorldPrices.query.join(Products,
        WorldPrices.productsid==Products.productid).add_columns(Products.product,
        WorldPrices.productsid, WorldPrices.worldid,
        WorldPrices.price, WorldPrices.amount).filter(WorldPrices.worldid ==
        worldid).all()
