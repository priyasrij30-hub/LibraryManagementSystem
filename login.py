# Login Feature

users = {"admin": "admin123"}

def login(username, password):
    if users.get(username) == password:
        return "Login Successful"
    return "Login Failed"

print(login("admin", "admin123"))
