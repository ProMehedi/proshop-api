def userSchema(user) -> dict:
    return {
        'id': str(user['_id']),
        'firstName': user['firstName'],
        'lastName': user['lastName'],
        'email': user['email'],
        'username': user['username'],
        'avatar': user['avatar'],
        'phone': user['phone'],
        'company': user['company'],
        'password': user['password'] if 'password' in user else None,
        'role': user['role'],
        'createdAt': user['created_at'],
        'shipping': user['shipping'],
        'billing': user['billing'],
        'verified': user['verified'],
        'otp': user['otp'],
    }


def userListSchema(users) -> list:
    return [userSchema(user) for user in users]
