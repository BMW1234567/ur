import json
import os
from app import register_user, FILE_PATH

def setup_function():
    # Перед каждым тестом очищаем файл
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump({}, f)

def test_register_new_user():
    result = register_user("alex", "12345")
    assert result == "Пользователь успешно зарегистрирован."
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "alex" in data
    assert data["alex"] == "12345"

def test_register_existing_user():
    register_user("alex", "12345")
    result = register_user("alex", "67890")
    assert result == "Пользователь с таким логином уже существует."
