from flask import Blueprint, request
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from ..models.user import User
from ..configs.db import db
from ..schemas.user import userSchema, userListSchema

user = Blueprint('user', __name__)


@user.post('/register')
def register_user():
    if not request.data:
        return {"success": False, "message": "No data provided"}, 400

    if not request.is_json:
        return {"success": False, "message": "Invalid data, Only JSON data can be pass"}, 400

    if not request.json.get('firstName'):
        return {"success": False, "message": "First Name is required"}, 400

    if not request.json.get('lastName'):
        return {"success": False, "message": "Last Name is required"}, 400

    if not request.json.get('email'):
        return {"success": False, "message": "Email is required"}, 400

    if not request.json.get('phone'):
        return {"success": False, "message": "Phone is required"}, 400

    if not request.json.get('password'):
        return {"success": False, "message": "Password is required"}, 400

    # Check for existing user with email
    existingUser = db.users.find_one({'email': request.json.get('email')})
    if existingUser:
        return {"success": False, "message": "User already exists with this email"}, 400

    user = User(
        first_name=request.json.get('firstName'),
        last_name=request.json.get('lastName'),
        email=request.json.get('email'),
        phone=request.json.get('phone'),
        password=generate_password_hash(request.json.get('password'))
    )

    new_user = db.users.insert_one(dict(user))
    created_user = db.users.find_one({'_id': new_user.inserted_id})
    return {
        "success": True,
        "message": "User registered successfully",
        "data": userSchema(created_user)
    }, 201


@user.post('/login')
def login_user():
    if not request.data:
        return {"success": False, "message": "No data provided"}, 400

    if not request.is_json:
        return {"success": False, "message": "Invalid data, Only JSON data can be pass"}, 400

    if not request.json.get('email'):
        return {"success": False, "message": "Email is required"}, 400

    if not request.json.get('password'):
        return {"success": False, "message": "Password is required"}, 400

    user = db.users.find_one({'email': request.json.get('email')})

    if not user:
        return {"success": False, "message": "User not found"}, 404

    if not check_password_hash(user['password'], request.json.get('password')):
        return {"success": False, "message": "Invalid credentials"}, 400

    return {
        "success": True,
        "message": "User logged in successfully",
        "data": userSchema(user),
        "token": create_access_token({'id': str(user['_id'])})
    }, 200


@user.get('/profile')
@jwt_required()
def get_user_profile():
    identity = get_jwt_identity()
    if not identity:
        return {"success": False, "message": "Not authorized! Invalid token"}, 401

    user = db.users.find_one({'_id': ObjectId(identity['id'])})
    if not user:
        return {"success": False, "message": "User not found"}, 404

    return {"success": True, "message": "User profile fetched successfully", "data": userSchema(user)}, 200


@user.put('/profile')
@jwt_required()
def update_user_profile():
    if not request.is_json:
        return {"success": False, "message": "Invalid data, Only JSON data can be pass"}, 400

    identity = get_jwt_identity()
    if not identity:
        return {"success": False, "message": "Not authorized! Invalid token"}, 401

    user = db.users.find_one({'_id': ObjectId(identity['id'])})

    if not user:
        return {"success": False, "message": "User not found"}, 404

    if request.json.get('firstName'):
        user['first_name'] = request.json.get('firstName')

    if request.json.get('lastName'):
        user['last_name'] = request.json.get('lastName')

    if request.json.get('phone'):
        user['phone'] = request.json.get('phone')

    if request.json.get('password'):
        user['password'] = generate_password_hash(request.json.get('password'))

    db.users.update_one({'_id': user['_id']}, {'$set': user})

    return {"success": True, "message": "User profile updated successfully", "data": userSchema(user)}, 200


@user.get('/all')
@jwt_required()
def get_all_users():
    identity = get_jwt_identity()
    if not identity:
        return {"success": False, "message": "Not authorized! Invalid token"}, 401

    user = db.users.find_one({'email': identity['email']})
    if not user['role'] == 'admin':
        return {"success": False, "message": "Not authorized! You are not an admin"}, 401

    users = db.users.find()
    return {"success": True, "message": "All users fetched successfully", "data": userListSchema(users)}, 200


@user.get('/<id>')
@jwt_required()
def get_user_by_id(id):
    identity = get_jwt_identity()
    if not identity:
        return {"success": False, "message": "Not authorized! Invalid token"}, 401

    user = db.users.find_one({'_id': ObjectId(identity['id'])})
    if not user['role'] == 'admin':
        return {"success": False, "message": "Not authorized! You are not an admin"}, 401

    user = db.users.find_one({'_id': ObjectId(id)})
    if not user:
        return {"success": False, "message": "User not found"}, 404

    return {"success": True, "message": "User fetched successfully", "data": userSchema(user)}, 200
