def calculator(num1: float, operator: str, num2: float) -> float:
    """
    Функция для выполнения арифметических операций между двумя числами.

    Параметры:
    num1 (float): Первое число.
    operator (str): Арифметический оператор ('+', '-', '*', '/', '//', '%', '**').
    num2 (float): Второе число.

    Возвращает:
    float: Результат арифметической операции.

    Исключения:
    ValueError: Если передан некорректный оператор или нечисловые значения.
    ZeroDivisionError: Если происходит попытка деления на ноль.
    """
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return num1 / num2
        elif operator == '//':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return num1 // num2
        elif operator == '%':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return num1 % num2
        elif operator == '**':
            return num1 ** num2
        else:
            raise ValueError(f"Некорректный оператор: {operator}")
    except TypeError:
        raise ValueError("Неверный тип данных. Оба аргумента должны быть числами.")