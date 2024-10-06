mentors = ['Тимур', 'Арсен', 'Гулина',  'Даниель']

while True:
    print("выберите команду")
    print("1)добавление метора")
    print("2)измените имя ментора")
    print("3)удаления метора")
    print("0)выход")

    function = int(input())
    if function == 1:
        choice = input("Введите нового ментора:")
        choice = choice.title()

        if choice in mentors:
            print('Это имя уже есть в списке')
            mentors.pop(-1)
            continue
        mentors.append(choice)
        add = len(mentors)
        print(f'количество менторов ({add}) на данный момент')

        if len(choice) > 15:
            print('Имя не должно содержать 15 букв')
            continue

        if len(mentors) > 10:
            mentors.pop(-1)
            print("количества менторов больше 10.")
            continue

        print(mentors)

    elif function == 2:
        name = input("Введите имя измененяемого ментора:")
        name_n = input("Введите нового ментора:")
        name = name.title()
        name_n = name_n.title()

        if name_n in mentors:
            print('Это имя уже есть в списке')

        if len(name_n) >= 15:
            print("имя не должно содержать 15 букв")

        elif name not in mentors:
            print("в списке нет такого имени")

        if name in mentors:
            index = mentors.index(name)
            mentors[index] = name_n
            print(mentors)

    elif function == 3:
        deletion = input("Введите имя или индекс чтобы удалить:")
        deletion = deletion.title()

        if deletion.isnumeric():
            deletion1 = int(deletion)
            mentors.pop(deletion1)
            print(mentors)

        elif deletion in mentors:
            name2 = mentors.index(deletion)
            mentors.pop(name2)
            print(mentors)

        else:
            print("такого имени нет в списке")

    elif function == 0:
        print(tuple(mentors))
        break

    else:
        print("введите номер функции")
