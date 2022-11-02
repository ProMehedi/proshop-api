from flask import Blueprint, request
from .models.user import User
from .config import db
from .schemas.user import userSchema

auth = Blueprint('auth', __name__)


@auth.post('/register')
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

    user = User(
        first_name=request.json.get('firstName'),
        last_name=request.json.get('lastName'),
        email=request.json.get('email'),
        phone=request.json.get('phone'),
        password=request.json.get('password')
    )

    new_user = db.users.insert_one(dict(user))
    created_user = db.users.find_one({'_id': new_user.inserted_id})
    return {
        "success": True,
        "message": "User registered successfully",
        "data": userSchema(created_user)
    }, 201
