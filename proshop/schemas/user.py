def userSchema(user) -> dict:
    return {
        'id': str(user['_id']),
        'firstName': user['firstName'],
        'lastName': user['lastName'],
        'email': user['email'],
        'phone': user['phone'],
        'password': user['password'] if 'password' in user else None,
        'role': user['role'],
        'createdAt': user['created_at'],
        'address': user['address']
    }


def userListSchema(users) -> list:
    return [userSchema(user) for user in users]
