# Считываем выражение с клавиатуры
expression = input().strip()

# Разделяем выражение на число1, операцию и число2
try:
    num1, operation, num2 = expression.split()
    num1 = int(num1)  # Преобразуем число1 в целое число
    num2 = float(num2)  # Преобразуем число2 в дробное число
except ValueError:
    print("Неверный формат ввода.")
    exit()

# Проверяем, что числа неотрицательные
if num1 < 0 or num2 < 0:
    print("Числа должны быть неотрицательными.")
    exit()

# Вычисляем результат в зависимости от операции
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Деление на ноль невозможно.")
        exit()
    result = num1 / num2
elif operation == '%':
    if num2 == 0:
        print("Деление на ноль невозможно.")
        exit()
    result = num1 % num2
else:
    print("Неверная операция.")
    exit()

# Округляем результат до двух знаков после запятой, если необходимо
if isinstance(result, float):
    result = round(result, 2)

# Выводим результат
print(f"Результат: {result}")