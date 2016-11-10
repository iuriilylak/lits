import random
value = ["камінь", "ножиці" ,"папір" ]
comp_chose = random.choice(value)


while True:
    you_chose = input('Вибери камінь , ножиці або папір     ')
    comp_chose = random.choice(value)
    if you_chose not in value:
        print('Ти дурак, вибери камінь , ножиці або папір')
        end = input('хочеш продовжити? натисни будь-яку клавішу   ')
        if end=="ні" :
            print("До побачення , СЛАБАК")
            break
        else:
            print("Ок , попробуємо ще раз")
            continue

    elif you_chose == comp_chose:
        print('Компютер викинув   ' + comp_chose)
        print('Нічия')
        end = input('хочеш продовжити? натисни будь-яку клавішу   ')
        if end == "ні":
            print("До побачення , СЛАБАК")
            break
        else:
            print("Ок , попробуємо ще раз")
            continue

    elif you_chose == "папір" and comp_chose == "ножиці":
        print('Компютер викинув   ' + comp_chose)
        print('Ти програв')
        end = input('хочеш продовжити? натисни будь-яку клавішу   ')
        if end == "ні":
            print("До побачення , СЛАБАК")
            break
        else:
            print("Ок , попробуємо ще раз")
            continue

    elif you_chose == "папір" and comp_chose == "камінь":
        print('Компютер викинув   ' + comp_chose)
        print('Ти переміг')
        end = input('хочеш продовжити? натисни будь-яку клавішу   ')
        if end == "ні":
            print("До побачення , СЛАБАК")
            break
        else:
            print("Ок , попробуємо ще раз")
            continue

    elif you_chose == "камінь" and comp_chose == "ножиці":
        print('Компютер викинув   ' + comp_chose)
        print('Ти переміг')
        end = input('хочеш продовжити? натисни будь-яку клавішу   ')
        if end == "ні":
            print("До побачення , СЛАБАК")
            break
        else:
            print("Ок , попробуємо ще раз")
            continue

    elif you_chose == "камінь" and comp_chose == "папір":
        print('Компютер викинув   ' + comp_chose)
        print('Ти програв')
        end = input('хочеш продовжити? натисни будь-яку клавішу   ')
        if end == "ні":
            print("До побачення , СЛАБАК")
            break
        else:
            print("Ок , попробуємо ще раз")
            continue
    elif you_chose == "ножиці" and comp_chose == "камінь":
        print('Компютер викинув   ' + comp_chose)
        print('Ти програв')
        end = input('хочеш продовжити? натисни будь-яку клавішу   ')
        if end == "ні":
            print("До побачення , СЛАБАК")
            break
        else:
            print("Ок , попробуємо ще раз")
            continue
    elif you_chose == "ножиці" and comp_chose == "папір":
        print('Компютер викинув   ' + comp_chose)
        print('Ти переміг')
        end = input('хочеш продовжити? натисни будь-яку клавішу   ')
        if end == "ні":
            print("До побачення , СЛАБАК")
            break
        else:
            print("Ок , попробуємо ще раз")
            continue

