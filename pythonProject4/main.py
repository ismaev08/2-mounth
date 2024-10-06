lambda функции.обработка исключений.
lambda_fun = lambda n1,n2: n1

def up_first_letter(word: str) ->str:
    return word.title()

def show_words(some_funktion, words_list):
    for word in words_list:
        print(some_funktion(word))

cities = ['tokmok', 'kemin', 'kant']

show_words(up_first_letter,cities)
show_words(len, cities)
show_words(str.upper, citi
try:#проверяется код
    print(2 * 'dsd')
except:#отлавливает исключения
    print("some error")
else:#есди ошибки нет
    print("ok")
finally:#завкршение проверкию
 #    print("cheking finished!")



# перечислите алгеметрические операторы? 






