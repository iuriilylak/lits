import random
value = ["камінь", "ножиці", "папір"]


def choose():
    value = ["камінь", "ножиці", "папір"]
    comp = random.choice(value)
    you = input('Вибери камінь , ножиці або папір     ')
    return you, comp

def end_game():
    end = input('хочеш продовжити? натисни будь-яку клавішу   ')
    if end == "ні":
        print("Гуляй , СЛАБАК")
        return False
    else:
        print("Ок , попробуємо ще раз")
        return True

def lose(comp_choose):
    print('Компютер викинув   ' + comp_choose)
    print('Ти програв')
    end_game()

def win(comp_choose):
    print('Компютер викинув   ' + comp_choose)
    print('Ти переміг')
    end_game()

def pat(comp_choose):
    print('Компютер викинув   ' + comp_choose)
    print('Нічия')
    end_game()

def err():
    print('Ти дурак?!?! вибери камінь , ножиці або папір')
    end_game()

while True:
    you_choose , comp_choose = choose()
    if  you_choose not in value:
        err()
    elif you_choose == comp_choose:
        pat(comp_choose)
    elif you_choose == "папір" and comp_choose == "ножиці":
        lose(comp_choose)
    elif you_choose == "папір" and comp_choose == "камінь":
        win(comp_choose)
    elif you_choose == "камінь" and comp_choose == "ножиці":
        win(comp_choose)
    elif you_choose == "камінь" and comp_choose == "папір":
        lose(comp_choose)
    elif you_choose == "ножиці" and comp_choose == "камінь":
        lose(comp_choose)
    elif you_choose == "ножиці" and comp_choose == "папір":
        win(comp_choose)