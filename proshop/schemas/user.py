def userSchema(user) -> dict:
    return {
        'id': str(user['_id']),
        'firstName': user['first_name'],
        'lastName': user['last_name'],
        'email': user['email'],
        'phone': user['phone'],
        'password': user['password'],
        'role': user['role'],
        'createdAt': user['created_at']
    }


def userListSchema(users) -> list:
    return [userSchema(user) for user in users]
