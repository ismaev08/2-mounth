
while True:
    wavels = 0
    consonants = 0

    word = input("Введите ваше слово  (exit to go out): ")
    if word.lower() == "exit":
        break
    for i in word:
        if word.isalpha():
            if i.lower() == "а" or i.lower() == "a":
                wavels += 1
            elif i.lower() == "о" or i.lower() == "e":
                wavels += 1
            elif i.lower() == "у" or i.lower() == "i":
                wavels += 1
            elif i.lower() == "э" or i.lower() == "o":
                wavels += 1
            elif i.lower() == "ы" or i.lower() == "u":
                wavels += 1
            elif i.lower() == "я" or i.lower() == "y":
                wavels += 1
            elif i.lower() == "ё":
                wavels += 1
            elif i.lower() == "ю":
                wavels += 1
            elif i.lower() == "е":
                wavels += 1
            elif i.lower() == "и":
                wavels += 1
            else:
                consonants += 1

    total_quantity = wavels + consonants
    if wavels and consonants > 0:
        persentage1 = (wavels / total_quantity) * 100
        persentage2 = (consonants / total_quantity) * 100
    elif wavels == 0:
        print("нет глассных")
        continue
    elif consonants == 0:
        print("нет согласных")
        continue

    print("слово:", word)
    print("количество букв:", len(word))
    print("согласных:", consonants)
    print("гласных:", wavels)
    print("Процентное соотношение букв:", persentage1,"% /", persentage2,"%")