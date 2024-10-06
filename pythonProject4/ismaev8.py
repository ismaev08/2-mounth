# w - write
# a - add
# x - не создает файл с одинаковыми названиями
# контекстный менеджер "with", работа с файлами

# file = open('new_file.txt', 'w')
# file.write('что нибуть на кирилице (на русском) ')
# file.close()


# with open('new_file.txt', 'a') as file:
#     file.write('\n новая строка ')

# with open('other.txt', 'x') as new_file:
#     new_file.write('new data')


from time import sleep
with open('new_file.txt', 'r') as file:
    for i in file.readline():
        sleep(1)
        print(i, end='')

#file.redLine() пропускает строку
#print(file.read()) выводит букву по индексу
#print(file.readLine())выводит строку по индексу