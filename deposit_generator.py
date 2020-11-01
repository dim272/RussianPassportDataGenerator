import random

items = ["Кольцо","Цепь","Браслет","Крест","Серьги","Подвеска"]
number = list(range(0,10))
bigNumber = list(range(0,100))
ringSize = ["15,5","16","16,5","17","17,5","18","18,5","19","19,5","20","20,5","21","21,5","22","22,5","23","23,5",]
chainLengthList = list(range(40,76))
braceletLengthList = list(range(16,26))
color = ["красный", "зеленый", "синий", "белый", "черный", "розовый", "фиолетовый", "коричневый", "желтый", "голубой"]
colors = ["красные", "зеленые", "синие", "белые", "черные", "розовые", "фиолетовые", "коричневые", "желтые", "голубые"]

totalWeightList = []

def discardGenerator(n):
    x = n
    randomNumber = random.choice(list(range(2,11)))
    result = x/randomNumber
    return round(result, 2)

def itemGenerator():
    item = random.choice(items)

    if item == "Кольцо":
        size = random.choice(ringSize)
        weight = random.uniform(0.9,4.9)

        if random.choice(list(range(0, 2))) == 1:
           discard = str(f"Сброс: {(discardGenerator(weight))} на {random.choice(color)} камень")
        else:
            discard = "Чистое изделие"

        if random.choice(list(range(0, 6))) == 1:
            compound = str(", два сплава")
        else:
            compound = ""

        totalWeightList.append(round(weight, 2))
        return str(f"{item}, вес {round(weight, 2)}гр, размер {size}, ({discard}){compound}")

    elif item == "Серьги":
        weight = random.uniform(2.1, 6.9)
        if random.choice(list(range(0, 2))) == 1:
            discard = str(f"Сброс: {discardGenerator(weight)} на {random.choice(colors)} камни")
        else:
            discard = "Чистое изделие"

        if random.choice(list(range(0, 5))) == 1:
            compound = str(", два сплава")
        else:
            compound = ""

        totalWeightList.append(round(weight, 2))
        return str(f"{item}, вес {round(weight, 2)}гр ({discard}){compound}")

    elif item == "Крест":
        weight = random.uniform(0.45, 3.9)

        if random.choice(list(range(0, 3))) == 1:
            discard = str(f"Сброс: {discardGenerator(weight)} на {random.choice(colors)} камни")
        else:
            discard = "Чистое изделие"

        if random.choice(list(range(0, 5))) == 1:
            compound = str(", два сплава")
        else:
            compound = ""

        totalWeightList.append(round(weight, 2))
        return str(f"{item}, вес {round(weight, 2)}гр ({discard}){compound}")

    elif item == "Подвеска":
        weight = random.uniform(0.75, 3.9)

        if random.choice(list(range(0, 6))) == 5:
            discard = str(f"Сброс: {discardGenerator(weight)} на {random.choice(colors)} камни")
        else:
            discard = "Чистое изделие"

        if random.choice(list(range(0, 6))) == 5:
            compound = str(", два сплава")
        else:
            compound = ""

        totalWeightList.append(round(weight, 2))
        return str(f"{item}, вес {round(weight, 2)}гр ({discard}){compound}")

    elif item == "Браслет":
        length = random.choice(braceletLengthList)

        weight = random.uniform(6.1, 12.9)

        discard = str(f"Сброс: 0,{random.choice(list(range(1,6)))}гр на пружину")

        if random.choice(list(range(0, 6))) == 1:
            compound = str(", два сплава")
        else:
            compound = ""

        totalWeightList.append(round(weight, 2))
        return str(f"{item}, {length}см, вес {round(weight, 2)}гр ({discard}){compound}")

    elif item == "Цепь":
        length = random.choice(chainLengthList)
        weight = random.uniform(3.1, 21.9)
        discard = str(f"Сброс: 0,{random.choice(list(range(1, 6)))}гр на пружину")

        if random.choice(list(range(0, 6))) == 1:
            compound = str(", два сплава")
        else:
            compound = ""

        totalWeightList.append(round(weight, 2))
        return str(f"{item}, {length}см, вес {round(weight, 2)}гр ({discard}){compound}")

    else:
        return str("Ошибка по названию изделия")

def totalWeightCalculate():
    x = len(totalWeightList)
    sum = 0
    while x > 0:
        sum += totalWeightList[x-1]
        x -= 1
    totalWeightList.clear()
    return sum

def start():
    val = int(input("Сколько сгенерировать залогов? "))
    minNumberItems = int(input("Сколько изделий должно быть в одном билете минимум? "))

    if minNumberItems < 1:
        minNumberItems = 1
        print(f"Минимальное количесвто изделий в билете будет равно 1")

    maxNumberItems = int(input("Сколько изделий должно быть в одном билете маскимум? "))

    file = open(f'/home/let/Документы/PassGen/deposits.txt', "at")

    numberOfDeposit = 1

    while val > 0:
        randomItems = random.choice(list(range(minNumberItems, (maxNumberItems + 1))))
        file.write(str(f"ЗАЛОГОВЫЙ БИЛЕТ №{numberOfDeposit} \n "))
        file.write(str(f"В этом билете будет {randomItems} предмет(ов):\n "))
        while randomItems > 0:
            file.write(str(f"{itemGenerator()}\n "))
            randomItems -= 1
        file.write(str("\n"))
        file.write(str(f"Общий вес = {round(totalWeightCalculate(), 2)}гр \n \n \n "))
        numberOfDeposit += 1
        val -= 1

    file.close()

    print(f"Готово! Результат записан в файл {file}")

start()