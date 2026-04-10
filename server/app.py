from flask import make_response
from config import app
from flask import request, session
from models import User
from config import db


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