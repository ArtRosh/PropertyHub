from flask_sqlalchemy import SQLAlchemy
from config import db
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt


class Property(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)

    reviews = db.relationship("Review", back_populates="property", cascade="all, delete-orphan")
    images = db.relationship("Image", back_populates="property", cascade="all, delete-orphan")
    property_users = db.relationship("PropertyUser", back_populates="property", cascade="all, delete-orphan")


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String)
    role = db.Column(db.String, default="visitor")

    property_users = db.relationship("PropertyUser", back_populates="user", cascade="all, delete-orphan")

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password is not readable")

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)

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


class PropertyUser(db.Model):
    __tablename__ = "property_users"

    id = db.Column(db.Integer, primary_key=True)

    property_id = db.Column(db.Integer, db.ForeignKey("properties.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    property = db.relationship("Property", back_populates="property_users")
    user = db.relationship("User", back_populates="property_users")