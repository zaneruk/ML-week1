# Функция для проверки сложности пароля
def check_password_strength(password):
    # Проверка длины пароля
    if len(password) < 8:
        return "Слабый пароль"

    # Критерии сложности
    has_upper = any(char.isupper() for char in password)  # Прописные буквы
    has_lower = any(char.islower() for char in password)  # Строчные буквы
    has_digit = any(char.isdigit() for char in password)  # Цифры
    has_special = any(char in '!@#$%^&*(),.?":{}|<>' for char in password)  # Специальные символы

    # Подсчет количества выполненных критериев
    criteria_count = sum([has_upper, has_lower, has_digit, has_special])

    # Определение сложности пароля
    if criteria_count == 4:
        return "Сильный пароль"
    elif criteria_count == 3:
        return "Средний пароль"
    else:
        return "Слабый пароль"

# Ввод пароля
password = input().strip()

# Проверка сложности пароля и вывод результата
print(check_password_strength(password))