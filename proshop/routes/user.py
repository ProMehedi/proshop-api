from flask import Blueprint, request
from werkzeug.security import generate_password_hash
from ..models.user import User
from ..configs.db import db
from ..schemas.user import userSchema

user = Blueprint('user', __name__)


@user.post('/register')
def register_user():
    if not request.data:
        return {"success": False, "message": "No data provided"}, 400

    if not request.is_json:
        return {"success": False, "message": "Invalid data, Only JSON data can be expected"}, 400

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
