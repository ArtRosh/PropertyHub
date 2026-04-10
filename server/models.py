from flask_sqlalchemy import SQLAlchemy
from config import db


class Property(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)

    reviews = db.relationship("Review", back_populates="property", cascade="all, delete-orphan")
    images = db.relationship("Image", back_populates="property", cascade="all, delete-orphan")


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)

    property_id = db.Column(db.Integer, db.ForeignKey("properties.id"))
    property = db.relationship("Property", back_populates="reviews")


class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)

    property_id = db.Column(db.Integer, db.ForeignKey("properties.id"))
    property = db.relationship("Property", back_populates="images")