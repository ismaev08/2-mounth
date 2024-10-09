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

    def call(self, sim_card_number, call_to_number):
        sim_card = self._sim_cards_list[sim_card_number - 1] if sim_card_number <= len(self._sim_cards_list) else ""
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")

