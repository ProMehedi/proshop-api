def productSchema(product) -> dict:
    return {
        'id': str(product['_id']),
        'name': product['name'],
        'slug': product['slug'],
        'desc': product['desc'],
        'shortDesc': product['shortDesc'],
        'price': product['price'],
        'regularPrice': product['regularPrice'],
        'categories': product['categories'],
        'type': product['type'],
        'status': product['status'],
        'featured': product['featured'],
        'stockQuantity': product['stockQuantity'],
        'sku': product['sku'],
        'thumbnail': product['thumbnail'],
        'images': product['images'],
        'attributes': product['attributes'],
        'userId': str(product['userId']),
    }


def productListSchema(products) -> list:
    return [productSchema(product) for product in products]
