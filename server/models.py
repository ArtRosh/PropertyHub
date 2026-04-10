from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy

from config import bcrypt,db


class Property(db.Model , SerializerMixin):
    __tablename__='properties'

    serialize_rules = ('-property_users.property', '-images.property', '-reviews.property')
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    description = db.Column(db.String)
    amenities = db.Column(db.String)
    availability = db.Column(db.String)
    image = db.Column(db.String)
    reservation = db.Column(db.String)
    
    property_users = db.relationship('PropertyUser', back_populates='property', cascade='all, delete-orphan')

    images = db.relationship('Image', back_populates='property', cascade='all, delete-orphan')

    reviews = db.relationship('Review', back_populates='property', cascade='all, delete-orphan')

    @validates('name')
    def validates_name(self, key, name):
        if name:
            return name
        else:
            raise ValueError("The property must have a name.")
    
    @validates('address')
    def validates_address(self, key, address):
        if address:
            return address
        else:
            raise ValueError("The property must have an address.")
        
    @validates('description')
    def validates_description(self, key, description):
        if description:
            return description
        else:
            raise ValueError("The property must have a description.")
        
    

class Review(db.Model, SerializerMixin):
    __tablename__='reviews'

    serialize_rules = ('-property.reviews', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))

    property = db.relationship('Property', back_populates='reviews')

    @validates('name')
    def validates_name(self, key, name):
        if name:
            return name
        else:
            raise ValueError("The review must have name.")
        
    @validates('email')
    def validates_email(self, key, email):
        if email:
            return email
        else:
            raise ValueError("The review must have an email.")
        
    @validates('rating')
    def validates_rating(self, key, rating):
        if 0 <= rating <= 5:
            return rating
        else:
            raise ValueError("The reviews rating must btween 0 and 5 ,inclusively.")
        


class User(db.Model, SerializerMixin):
    __tablename__='users'

    serialize_rules = ('-property_users.user', )

    ROLES = [
        ('admin', 'Administrator'),
        ('visitor', 'Visitor'),
    ]


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String)
    role = db.Column(db.String, default='visitor')

    property_users = db.relationship('PropertyUser', back_populates='user', cascade='all, delete-orphan')

    @hybrid_property
    def password_hash(self):
        raise AttributeError("You don't have permission to view the password!")
    
    @password_hash.setter
    def password_hash(self, password):
        print(password.encode('utf-8'))
        new_hashed_password = bcrypt.generate_password_hash(password.encode('utf-8'))

        self._password_hash = new_hashed_password.decode('utf-8')

    def authenticate(self, password):
        # check if inputed password matches user's password
        print(password)
        print(self._password_hash)
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))



    @validates('username')
    def validates_username(self, key, username):
        if 0 < len(username) < 20:
            return username
        else:
            raise ValueError("The username must be betwen 0 and twenty characters.")
        
    @validates('password')
    def validates_password(self,key, password):

        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

        if not pattern == password:
            return password
        else:
            raise ValueError("Invalid password! Password should be at least 8 characters long and contain at least one lowercase letter, one digit, and one special character (@ $ ! % * ? &)")
        

    
class Image(db.Model, SerializerMixin):
    __tablename__='images'

    serialize_rules = ('-property.images',)

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))

    property = db.relationship('Property', back_populates='images')

    @validates('image')
    def validates_image(self, key, image):
        if image:
            return image
        else:
            raise ValueError("The image must be a image.")



class PropertyUser(db.Model, SerializerMixin):
    __tablename__='property_users'

    serialize_rules = ('-property.property_users', '-user.property_users')

    id = db.Column(db.Integer, primary_key=True)

    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    property = db.relationship('Property', back_populates='property_users')

    user = db.relationship('User', back_populates='property_users')

    



