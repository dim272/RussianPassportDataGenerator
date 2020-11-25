import random

items = ["Кольцо", "Цепь", "Браслет", "Крест", "Серьги", "Подвеска"]
items2 = ["Монета", "Зубные коронки"]
number = list(range(0, 10))
bigNumber = list(range(0, 100))
ringSize = ["15,5", "16", "16,5", "17", "17,5", "18", "18,5", "19", "19,5", "20", "20,5", "21", "21,5", "22", "22,5",
            "23", "23,5", ]
chain_length_list = list(range(40, 76))
bracelet_length_list = list(range(16, 26))
color = ["красный", "зеленый", "синий", "белый", "черный", "розовый", "фиолетовый", "коричневый", "желтый", "голубой"]
colors = ["красные", "зеленые", "синие", "белые", "черные", "розовые", "фиолетовые", "коричневые", "желтые", "голубые"]
gold = [375, 500, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 585, 583, 750]

total_weight_list = []


def discard_generator(n):
    x = n
    random_number = random.choice(list(range(2, 11)))
    result = x / random_number
    return round(result, 2)


def item_generator():
    if random.choice(list(range(0,7))) < 5:
        item = random.choice(items)
    else:
        item = random.choice(items2)

    if random.choice(list(range(0, 10))) < 8:
        have_tag = 'бирка есть'
    else:
        have_tag = 'бирки нет'

    if random.choice(list(range(0, 10))) > 1:
        have_probe = 'клеймо есть'
    else:
        have_probe = 'клейма нет'

    if item == "Кольцо":
        size = random.choice(ringSize)
        weight = random.uniform(0.9, 3.9)
        probe = random.choice(gold)

        if random.choice(list(range(0, 2))) == 1:
            discard = str(f"Сброс: {(discard_generator(weight))} на {random.choice(color)} камень")
        else:
            discard = "Чистое изделие"

        if random.choice(list(range(0, 6))) == 1:
            compound = str(", два сплава")
        else:
            compound = ""

        total_weight_list.append(round(weight, 2))
        return str(f"{item}, проба {probe}, вес {round(weight, 2)}гр, ({discard}), {have_probe}, {have_tag}, размер {size}{compound}")

    elif item == "Серьги":
        weight = random.uniform(2.1, 5.9)
        probe = random.choice(gold)

        if random.choice(list(range(0, 2))) == 1:
            discard = str(f"Сброс: {discard_generator(weight)} на {random.choice(colors)} камни")
        else:
            discard = "Чистое изделие"

        if random.choice(list(range(0, 5))) == 1:
            compound = str(", два сплава")
        else:
            compound = ""

        total_weight_list.append(round(weight, 2))
        return str(f"{item}, проба {probe}, вес {round(weight, 2)}гр, ({discard}), {have_probe}, {have_tag}{compound}")

    elif item == "Крест":
        weight = random.uniform(0.45, 2.9)
        probe = random.choice(gold)

        if random.choice(list(range(0, 3))) == 1:
            discard = str(f"Сброс: {discard_generator(weight)} на {random.choice(colors)} камни")
        else:
            discard = "Чистое изделие"

        if random.choice(list(range(0, 5))) == 1:
            compound = str(", два сплава")
        else:
            compound = ""

        total_weight_list.append(round(weight, 2))
        return str(f"{item}, проба {probe}, вес {round(weight, 2)}гр, ({discard}), {have_probe}, {have_tag}{compound}")

    elif item == "Подвеска":
        weight = random.uniform(0.50, 2.9)
        probe = random.choice(gold)

        if random.choice(list(range(0, 6))) == 5:
            discard = str(f"Сброс: {discard_generator(weight)} на {random.choice(colors)} камни")
        else:
            discard = "Чистое изделие"

        if random.choice(list(range(0, 6))) == 5:
            compound = str(", два сплава")
        else:
            compound = ""

        total_weight_list.append(round(weight, 2))
        return str(f"{item}, проба {probe}, вес {round(weight, 2)}гр, ({discard}), {have_probe}, {have_tag}{compound}")

    elif item == "Браслет":
        length = random.choice(bracelet_length_list)
        probe = random.choice(gold)

        weight = random.uniform(3.1, 9.9)

        discard = str(f"Сброс: 0,{random.choice(list(range(1, 3)))}гр на пружину")

        if random.choice(list(range(0, 6))) == 1:
            compound = str(", два сплава")
        else:
            compound = ""

        total_weight_list.append(round(weight, 2))
        return str(f"{item}, проба {probe}, вес {round(weight, 2)}гр, ({discard}), {have_probe}, {have_tag}, {length}см{compound}")

    elif item == "Цепь":
        length = random.choice(chain_length_list)
        weight = random.uniform(4.1, 18.9)
        probe = random.choice(gold)
        discard = str(f"Сброс: 0,{random.choice(list(range(1, 3)))}гр на пружину")

        if random.choice(list(range(0, 6))) == 1:
            compound = str(", два сплава")
        else:
            compound = ""

        total_weight_list.append(round(weight, 2))
        return str(f"{item}, проба {probe}, вес {round(weight, 2)}гр, ({discard}), {have_probe}, {have_tag}, {length}см{compound}")

    elif item == "Зубные коронки":
        weight = random.uniform(0.9, 3.99)
        probe = 850

        if random.choice(list(range(0, 6))) == 1:
            discard = str(f"Сброс: {round(weight / random.choice(list(range(5, 11))), 2)}гр на загрязнение")
        else:
            discard = "Чистые"

        total_weight_list.append(round(weight, 2))
        return str(f"{item}, проба {probe}, вес {round(weight, 2)}гр ({discard})")

    elif item == "Монета":
        rating_coin = [5, 10, 15]
        weight = 0
        coin = 0
        probe = 0

        random_coin = random.choice(list(range(1, 7)))

        if random_coin <= 4:
            what_coin = random.choice(rating_coin)
            coin = f"Николаевская {what_coin} руб"
            probe = 900

            if what_coin == 5:
                weight = 4.3
            elif what_coin == 10:
                weight = 7.7
            elif what_coin == 15:
                weight = 11.6

        elif random_coin == 5:
            coin = f"Сбербанк 50 руб"
            probe = 999
            weight = 7.78

        elif random_coin == 6:
            coin = f"Один червонец (сеятель)"
            probe = 585
            weight = 7.74

        total_weight_list.append(weight)
        return str(f"{item}, проба {probe}, вес {weight}гр ({coin})")

    else:
        return str("Ошибка по названию изделия")


def total_weight_calculate():
    x = len(total_weight_list)
    sum = 0
    while x > 0:
        sum += total_weight_list[x - 1]
        x -= 1
    total_weight_list.clear()
    return sum


def start():
    val = int(input("Сколько сгенерировать залогов? "))
    minNumberItems = int(input("Сколько изделий должно быть в одном билете минимум? "))

    if minNumberItems < 1:
        minNumberItems = 1
        print(f"Минимальное количесвто изделий в билете будет равно 1")

    maxNumberItems = int(input("Сколько изделий должно быть в одном билете маскимум? "))

    file = open(f'deposits.txt', "at")

    numberOfDeposit = 1

    while val > 0:
        randomItems = random.choice(list(range(minNumberItems, (maxNumberItems + 1))))
        file.write(str(f"ЗАЛОГОВЫЙ БИЛЕТ №{numberOfDeposit} \n "))
        file.write(str(f"В этом билете будет {randomItems} предмет(ов):\n "))
        while randomItems > 0:
            file.write(str(f"{item_generator()}\n "))
            randomItems -= 1
        file.write(str("\n"))
        file.write(str(f"Общий вес = {round(total_weight_calculate(), 2)}гр \n \n \n "))
        numberOfDeposit += 1
        val -= 1

    file.close()

    print(f"Готово! Результат записан в файл.")


start()
