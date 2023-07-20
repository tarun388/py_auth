from user import user_password

def validate(user, password):
    if (user, password) in user_password: return True
    return False