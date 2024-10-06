#операторы:принадлежности, назначения. цикл.
# number = 5
# number += 5
# number -= 3
# number **= 2
# number *= 0.5
# print(number)


"""операторы пренадлежности"""

# word = 'geeks'
# print('g' in word)
# print('g' not in word)
# print('t' in word)
# print('t' not in word)
#
# counter = 0
#
# while counter < 100:
#     if counter == 70:
#         print('stop')
#         break
#     counter += 1
#     if counter % 2 == 0:
#         continue
#     print('geeks',counter)

#
# word = 'Kyrgyzstan'.upper()
# for letter in word:
#     if letter == 'S':
#         break
#     if letter in 'RYSZ':
#         continue
#     print(letter)
#
#
#
# day = int(input('ваш день рождения (1-31):'))
#
# month = input('ваш месяца (1-12):')
#
# if (month == "01" and day >=20) or (month =="02" and day <= 19):
#     print('водолeй')
#
# elif(month == "02" and day >=20) or (month == "03" and day <= 20):
#     print('рыба')
#
# elif (month == "03" and day >= 21) or (month == "04" and day <= 20):
#     print('овен')
#
# elif (month == "04" and day >= 21 ) or (month == "05" and day <= 21):
#     print('телец')
#
# elif (month == "05"  and day >=22 ) or (month == "06"  and day <= 21 ):
#     print('близнецы')
#
# elif (month == "06" and day >= 22) or (month == "07" and day <= 22):
#     print('рак')
#
# elif (month == "07" and day >= 23) or (month == "08" and day <= 21):
#     print('лев')
#
# elif (month == "08" and day >= 22) or (month == "09" and day <= 23):
#     print('дева')
#
# elif (month == "09" and day >= 24 ) or (month == "10" and day <= 23):
#     print('весы')
#
# elif (month == "10" and day >= 24) or (month == "11" and day <= 22):
#     print('скорпион')
#
# elif (month == "11" and day >= 23) or (month == "12" and day <= 22):
#     print('стрелец')
#
# elif (month == "12" and day >= 23) or (month == "01" and day <= 20):
#     print('козерог')
#
# else:
#     print('ошибка ввода!!!!!')




def get_item_by_index(iterable):
    while True:
        try:
            index = int(input("Введите индекс элемента (для выхода введите 'exit'): "))
            if isinstance(iterable, (list, tuple, str)):
                if 0 <= index < len(iterable):
                    print(f"Элемент по индексу {index}: {iterable[index]}")
                else:
                    print(f"Индекс {index} выходит за границы списка ({0} до {len(iterable)-1})")
            else:
                print("Неподдерживаемый тип данных. Поддерживаются только списки, кортежи и строки.")
        except ValueError:
            command = input("Введите 'exit' для завершения: ").strip().lower()
            if command == 'exit':
                break
            else:
                print("Некорректный ввод, попробуйте снова.")

# Пример использования:
my_list = [10, 20, 30, 40, 50]
get_item_by_index(my_list)
















