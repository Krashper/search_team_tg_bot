users = {
    953314440: {
        'lang': 'Русский',
        'name': 'имя',
        'username': 'lfda',
        'age': 32
    }
}

def check_register(user_id: int) -> bool:
    return user_id in users.keys()

def is_unique_name(name: str) -> bool:
    flag = True
    for user_id in users.keys():
        if name == users[user_id]['name']:
            flag = False
    return flag

def create_new_user(user_id: int, lang: str, name: str, username: str, age: int) -> None:
    users[user_id] = {
        'lang': lang,
        'name': name,
        'username': username,
        'age': age
    }
