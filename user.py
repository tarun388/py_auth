user_password = [
    ("tarun", "pass")
]

def existing_user(user):
    for (username, password) in user_password:
        if username == user: return True
    return False

def create_user(user, password):
    user_password.append((user, password))

def list_user():
    return user_password