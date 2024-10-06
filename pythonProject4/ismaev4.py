# Списки , кортежи.Индексы и срезы. Встроенные функции к наборам элементов
#Списковые включение list comprehesion.

students = ['danila', 'anuar', 'kanat', 'islam', 'danila']

# """Индексы"""
# print(students[1])
# print(students[2])
# print(students[0])
# print(students[-1])
# """срезы"""
# print(students[1:3])
# print(students[:2])
# print(students[-2:])

"""add"""
# students.append('nigina')#добавляет один обьект в конец
# students.insert(2,'sanvar')#добавляет один обьект в опр место
students.extend(['kerimkazy', 'abdurahim'])#добавляет более одного обьекта в конец
"""edit"""
# students.sort(reverse=True)
# students[-1] = 'selim'
# students[:2] = ['roman', 'amir']

print(students)
"""delete"""
# students.remove('anua')#удаление по значению
# deleted = students.pop(0)#удаление по индексу
# del students[::]#удаление более одного обьекта

# print(students.index('islam')).
# print(students.count('islam'))
# print(students)

# numbers = (45,)
# print(type(numbers))
#
# numbers = 23, 12, 45, 61, 98, 77
# print(numbers)
# print(numbers)
# print(type(numbers))


numbers = [0.6, 34, 12, 7.89, 23, 11]
#print(min(numbers)) #  показывает минимальнй обьект
#print(max(numbers)) #  показывает максимальный обьект
#print(all(numbers)) # находит не правильный обьект
#print(any(numbers)) # находит хоть 1 правильный обьект
#print(sorted(numbers)) # копирует список и сортирует

# rus = 'цукенгшщзхъфывапролджэячсмитьбю'
# eng = 'qwertyuiopasdfghjklzxcvbnm'


# print(rus[0])
# print(rus[eng.index('n')])





