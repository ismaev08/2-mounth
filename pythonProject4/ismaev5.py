# словари,множества.
# student = {
#      'name': 'azamat',
#      'age': 20
#
#
# """add"""
# student['height'] = 1.77
# student.update({'surname': 'abdrahimov', 'hobby': ['shess', 'boxing']})
#
#
# print(student)
# print(student['name'])
# print(student.get('ag', 'нет такого ключа'))


# """edit"""
# student['age'] = 22
# student{'name'} = student['name'].title()
#
# """delete"""
# delete = student.pop('age')
#
# print(student.keys())
#
#
# numbers1 = [1, 2, 3, 2, 4, 1, 5, 3,]
# numbers2 = (1, 2, 3, 2, 4, 1, 5, 3,)
# numbers3 = {1, 2, 3, 2, 4, 1, 5, 3,}
# print(numbers1, numbers2, numbers3, sep='\n')
#
beshbarmak = {"мясо", "лук", "лапша"}
plov = {"мясо", "рис", "морковь"}
#
# print(beshbarmak.union(plov))
# print(beshbarmak.difference(plov))
# print(beshbarmak.symmetric_difference(plov))
print(beshbarmak.intersection(plov))


# while True:
#     colors = input("Введите увет светофора (чтобы выйти нвпишите quit):").lower()
#
#     if colors == "красный":
#         print("стой")
#
#     elif colors == "желтый":
#         print("готовся")
#
#     elif colors == "зеленый":
#         print("поехали")
#
#     elif colors == "quit":
#         break
#
#     else:
#         print("Ведите цвет сфетофора")
#
#
# while

#Вводим кол-во дней для расчета общей и средней траты
# monday = int(input("Введите ваш расход за понедельник - "))
# tuesday = int(input("Введите ваш расход за вторник - "))
# wednesday = int(input("Введите ваш расход за среду - "))
# thursday = int(input("Введите ваш расход за четверг- "))
# friday = int(input("Введите ваш расход за пятницу- "))
# saturday = int(input("Введите ваш расход за субботу- "))
# sunday = int(input("Введите ваш расход за воскоресенье -"))
#
# #Общая сумма
# spending_for_week = monday+tuesday+wednesday+thursday+friday
# +saturday+sunday
#
# #Средняя сумма трат за день
# average_expense = (spending_for_week/int(7))
#
# #Округляем
# rounded = round(average_expense,1)
#
# #Вывод
# print('Ваш расход в неделю в общем составляет -$' f"{spending_for_week}")
#
# print('Ваш средний расход в день составляет -$' f"{rounded}")
#
#
#
# if average_expense <= 500 and average_expense >= 1:
#     print("you're spend low")
# elif average_expense >= 501 and average_expense <= 1500:
#     print("you spend a medium")
# elif average_expense >= 1501:
#     print("you're spend a lot")
# else:
#     print ("you don't spend anything")