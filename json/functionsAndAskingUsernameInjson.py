import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("whats your username")
    filename = 'username.json'
    with open(filename, "w") as file:
        json.dump(username, file)
    return username

def gree_user():
    username = get_stored_username()
    if username:
        print("welcome back "+username +" !")
    else:
        username = get_new_username()
        print("well remember you when you come back "+username)


gree_user()

