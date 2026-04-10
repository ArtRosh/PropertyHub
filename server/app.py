from flask import make_response
from config import app
from flask import request, session
from models import User
from config import db
from models import Property
from models import Review


@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    new_user = User(username=data['username'])
    new_user.password_hash = data['password']

    db.session.add(new_user)
    db.session.commit()

    session['user_id'] = new_user.id

    return new_user.to_dict(), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data['username']).first()

    if user and user.authenticate(data['password']):
        session['user_id'] = user.id
        return user.to_dict(), 200

    return {"error": "Invalid credentials"}, 401


@app.route('/logout', methods=['DELETE'])
def logout():
    session['user_id'] = None
    return {}, 204

@app.route('/check_session')
def check_session():
    user = User.query.get(session.get('user_id'))

    if user:
        return user.to_dict(), 200

    return {}, 401

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return [u.to_dict() for u in users], 200

@app.route('/properties', methods=['GET', 'POST'])
def properties():

    if request.method == 'GET':
        properties = Property.query.all()
        return [p.to_dict() for p in properties], 200

    if request.method == 'POST':
        data = request.get_json()

        new_property = Property(
            name=data['name'],
            location=data['location']
        )

        db.session.add(new_property)
        db.session.commit()

        return new_property.to_dict(), 201
    
@app.route('/properties/<int:id>', methods=['DELETE'])
def delete_property(id):
    user = User.query.get(session.get('user_id'))

    if not user or user.role != 'Admin':
        return {"error": "Unauthorized"}, 403

    property = Property.query.get(id)

    db.session.delete(property)
    db.session.commit()

    return {}, 204

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():

    if request.method == 'GET':
        reviews = Review.query.all()
        return [r.to_dict() for r in reviews], 200

    if request.method == 'POST':
        data = request.get_json()

        review = Review(
            name=data['name'],
            email=data['email'],
            rating=data['rating'],
            comment=data['comment'],
            property_id=data['property_id']
        )

        db.session.add(review)
        db.session.commit()

        return review.to_dict(), 201