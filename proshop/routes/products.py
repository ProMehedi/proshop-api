from flask import Blueprint, request
from pydantic import ValidationError
from bson.objectid import ObjectId
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models.product import Product
from ..schemas.product import productSchema
from ..configs.db import db

products = Blueprint('products', __name__)


@products.post('/new')
@jwt_required()
def create_product():
    identity = get_jwt_identity()
    if not identity:
        return {"success": False, "message": "Not authorized! Invalid token"}, 401

    user = db.users.find_one({'_id': ObjectId(identity['id'])})
    if not user:
        return {"success": False, "message": "User not found"}, 404

    if not request.data:
        return {"success": False, "message": "No data provided"}, 400

    if not request.is_json:
        return {"success": False, "message": "Invalid data, Only JSON data can be pass"}, 400

    try:
        product = Product(
            name=request.json.get('name'),
            slug=request.json.get('slug'),
            desc=request.json.get('desc'),
            shortDesc=request.json.get('shortDesc'),
            price=request.json.get('price'),
            regularPrice=request.json.get('regular_price'),
            categories=request.json.get('categories'),
            type=request.json.get('type') or 'simple',
            status=request.json.get('status') or 'draft',
            featured=request.json.get('featured') or False,
            stockQuantity=request.json.get('stockQuantity') or 0,
            sku=request.json.get('sku'),
            thumbnail=request.json.get('thumbnail'),
            images=request.json.get('images'),
            attributes=request.json.get('attributes') or [],
            userId=user['_id']
        )

        # print(dict(product))

        new_product = db.products.insert_one(dict(product))
        created_product = db.products.find_one(
            {'_id': new_product.inserted_id})

        return {
            "success": True,
            "message": "Product created successfully",
            "data": productSchema(created_product)
        }, 201
    except ValidationError as e:
        return {"success": False, "message": e.errors()}, 400
