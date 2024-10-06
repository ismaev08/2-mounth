# def get_data(name, surname='неизвестно'):
#     # print(f'name: {name}, surname: {surname}')
#     return f'name: {name}, surname: {surname}'
#
# get_data(surname ='ismaev', name ='selim')
# get_data('alina')



# lenght = 25
# width = 4
# square_3 = lenght * width
# print(square_3)
#
# def get_squsre(lenght, width: int)-> int:
#     """принимает ширину и длину,возврощает площадь."""
#     squsre = lenght * width
#     return squsre
# print(help((get_squsre)))

# squsre = get_square(25, 10)
# squsre_3 = get_square(8, 4)
#
# print(squsre)
# print(squsre_3)

# def menu(**kwargs):
#     return kwargs
#
# mondey = menu(eat='burger', drink= 'tea')
# print(mondey)
#
# from pprint import pprint
# expenses = 0
# days = 7
# for day in range(1, days+1):
#     input_expenses = int(input(f'day: {day} enter expenses'))
#     expenses += input_expenses
#     data[day] = input_expenses
#
# print(expenses)
# print(expenses/days)
# print(data)
# pprint(data,width=1
while True:
    data = tuple(map(int, input('enter expenses: ').split()))
    print(data)
    print(sum(data))
    print(sum(data) / len(data))

