import json
import os

FILE_PATH = "users.json"

def load_users():
    """Загрузка пользователей из файла"""
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_users(users):
    """Сохранение пользователей в файл"""
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def register_user(username, password):
    users = load_users()
    if username in users:
        return "Пользователь с таким логином уже существует."
    users[username] = password
    save_users(users)
    return "Пользователь успешно зарегистрирован."
