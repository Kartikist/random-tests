
from . import app, db
from .models import User
from flask import request, jsonify
import hashlib 
# CREATE: Add a new user
@app.route('/create', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], useremail=data['useremail'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(Message='Created successfully'), 200  # Change the status code to 201
# READ: Get a list of all users

@app.route('/read', methods=['GET'])
def read_users():
    user = User.query.first()
    if user:
        hashed_password = 'sha256' + hashlib.sha256(user.password.encode()).hexdigest()
        user_data = {'id': user.id, 'username': user.username, 'useremail': user.useremail, 'password': hashed_password}
        return jsonify(user_data)
    else:
        return jsonify(Message='No users found'), 404



# UPDATE: Update a user's username by ID
@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if user:
        user.username = data['username']
        db.session.commit()
        return jsonify(Message='Updated successfully'), 200
    return jsonify(Message='Check your user id'), 400

# DELETE: Delete a user by ID
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return '', 204  # No content
    return jsonify(Message='Check your user id'), 400
