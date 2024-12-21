# Menghubungkan ke DB
from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/db_water"
    mongo.init_app(app)
