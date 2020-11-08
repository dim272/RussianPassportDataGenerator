import random
from datetime import datetime
from russian_names import RussianNames

day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
       '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
yearOfBirth = list(range(1935, 1986))
yearOfIssue = list(range(1991, 2020))
houseApartmentNumbers = list(range(1, 299))
passportSeries = list(range(3700, 8999))
passportNumbers = list(range(101010, 990099))
departmentCode = list(range(100, 999))
phoneNumbers = list(range(1, 10))

cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Самара', 'Омск', 'Казань',
          'Челябинск', 'Ростов-на-Дону', 'Уфа', 'Пермь', 'Волгоград', 'Красноярск', 'Воронеж', 'Саратов', 'Краснодар',
          'Тольятти', 'Барнаул', 'Ижевск', 'Ульяновск', 'Ярославль', 'Владивосток', 'Хабаровск', 'Иркутск',
          'Новокузнецк', 'Тюмень', 'Оренбург', 'Кемерово', 'Рязань', 'Пенза', 'Набережные Челны', 'Астрахань', 'Липецк',
          'Тула', 'Томск', 'Киров', 'Махачкала', 'Чебоксары', 'Калининград', 'Брянск', 'Магнитогорск', 'Курск', 'Тверь',
          'Иваново', 'Нижний Тагил', 'Ставрополь', 'Белгород', 'Архангельск', 'Улан-Удэ', 'Владимир', 'Сочи', 'Калуга',
          'Курган', 'Орёл', 'Смоленск', 'Мурманск', 'Владикавказ', 'Череповец', 'Волжский', 'Чита', 'Саранск', 'Сургут',
          'Вологда', 'Тамбов', 'Комсомольск-на-Амуре', 'Кострома', 'Нальчик', 'Петрозаводск', 'Стерлитамак', 'Таганрог',
          'Якутск', 'Братск', 'Йошкар-Ола', 'Дзержинск', 'Орск', 'Шахты', 'Нижневартовск', 'Ангарск', 'Сыктывкар',
          'Новороссийск', 'Нижнекамск', 'Грозный', 'Бийск', 'Старый Оскол', 'Великий Новгород', 'Прокопьевск',
          'Рыбинск', 'Благовещенск', 'Норильск', 'Энгельс', 'Балаково', 'Петропавловск-Камчатский', 'Псков',
          'Северодвинск', 'Армавир', 'Златоуст', 'Балашиха', 'Химки', 'Каменск-Уральский', 'Подольск', 'Сызрань',
          'Новочеркасск', 'Королёв', 'Южно-Сахалинск', 'Волгодонск', 'Находка', 'Березники', 'Мытищи', 'Абакан',
          'Люберцы', 'Рубцовск', 'Салават', 'Майкоп', 'Уссурийск', 'Миасс', 'Ковров', 'Коломна', 'Электросталь',
          'Альметьевск', 'Пятигорск', 'Копейск', 'Назрань', 'Первоуральск', 'Кисловодск', 'Невинномысск', 'Одинцово',
          'Димитровград', 'Хасавюрт', 'Новочебоксарск', 'Новомосковск', 'Серпухов', 'Железнодорожный', 'Орехово-Зуево',
          'Муром', 'Камышин', 'Новый Уренгой', 'Нефтекамск', 'Черкесск', 'Ногинск', 'Нефтеюганск', 'Новошахтинск',
          'Щёлково', 'Елец', 'Новокуйбышевск', 'Ачинск', 'Ноябрьск', 'Сергиев Посад', 'Дербент', 'Октябрьский', 'Кызыл',
          'Северск', 'Арзамас', 'Обнинск', 'Ленинск-Кузнецкий', 'Киселёвск', 'Междуреченск', 'Ухта', 'Жуковский',
          'Элиста', 'Артём', 'Новотроицк', 'Батайск', 'Великие Луки', 'Тобольск', 'Магадан', 'Красногорск']
streets = ['Центральная', 'Молодежная', 'Школьная', 'Лесная', 'Советская', 'Новая', 'Садовая',
           'Набережная', 'Заречная', 'Зеленая', 'Мира', 'Ленина', 'Полевая', 'Луговая', 'Октябрьская', 'Комсомольская',
           'Гагарина', 'Первомайская', 'Северная', 'Солнечная', 'Степная', 'Южная', 'Береговая', 'Кирова', 'Пионерская',
           'Юбилейная', 'Речная', 'Нагорная', 'Восточная', 'Колхозная', 'Пушкина', 'Пролетарская', 'Железнодорожная',
           'Школьный', 'Озерная', 'Рабочая', 'Дачная', 'Победы', 'Калинина', 'Чапаева', 'Строителей', 'Заводская',
           'Совхозная', 'Кооперативная', 'Дружбы', 'Дорожная', 'Горького', 'Спортивная', 'Подгорная', 'Парковая',
           'Красноармейская', 'Красноармейская', 'Цветочная', 'Западная', 'Почтовая', 'Сосновая', 'Березовая',
           'Свободы', 'Строительная', 'Мичурина', 'Шоссейная', 'Чкалова', 'Партизанская', 'Вокзальная', 'Лесной',
           'Лермонтова', 'Московская', 'Садовый', 'Овражная', 'Трудовая', 'Клубная', 'Маяковского', 'Свердлова',
           'Фрунзе', 'Горная', 'Некрасова', 'Вишневая', 'Дзержинского', 'Труда', 'Гоголя', 'Карла Маркса', 'Красная',
           'Трактовая', 'Чехова', 'Весенняя', 'Зеленый', 'Верхняя', 'Коммунистическая', 'Энергетиков', 'Светлая',
           'Механизаторов', 'Куйбышева', 'Комарова', 'Больничная', 'Матросова', 'Новый', 'Родниковая', 'Майская',
           'Интернациональная', 'Островского', 'Островского', 'Советский', 'Северный', 'Южный', 'Нижняя', 'Молодежный',
           'Речной', 'Космонавтов', 'Крупской', 'Привокзальная', 'Суворова', 'Таежная', 'Сиреневая', 'Октябрьский',
           'Ключевая', 'Ломоносова', 'Центральный', 'Песчаная', 'Восточный', 'Тихая', 'Шевченко', 'Солнечный',
           'Коммунальная', 'Первомайский', 'Рябиновая', 'Комсомольский', 'Больничный', 'Новоселов', 'Пионерский',
           'Мостовая', 'Уральская', 'Транспортная', 'Почтовый', 'Ворошилова', 'Дальняя', 'К.Маркса', 'Широкая',
           'Буденного', 'Энтузиастов', 'Мирная', 'Сибирская', 'Луговой', 'Промышленная', 'Рабочий', 'Станционная',
           'Тургенева', 'Чернышевского', 'Магистральная', 'Кольцевая', 'Кольцевая', 'Титова', 'Приозерная', 'Урицкого',
           'Сельская', 'Российская', 'Ветеранов', 'Полевой', 'Целинная', 'Придорожная', 'Кирпичная', 'Профсоюзная',
           'Ленинская', 'Звездная', 'Ленинградская', 'Западный', 'Крестьянская', 'Энгельса', 'Гаражная', 'Песочная',
           'Орджоникидзе', 'Линейная', 'Толстого', 'Степной', 'Колхозный', 'Крайняя', 'Щорса', 'Есенина', 'Веселая',
           'Володарского', 'Запрудная', 'Луначарского', 'М.Горького', 'Герцена', 'Пугачева', 'Заводской', 'Мирный',
           'Кутузова', 'Заречный', 'Тихий', 'Фабричная', 'Дачный', 'Мелиораторов', 'Виноградная']
issued = ['Управление МВД России по Белгородской области ', 'Управление МВД России по Брянской области ',
          'Управление МВД России по Владимирской области ', 'Главное управление МВД России по Воронежской области ',
          'Управление МВД России по Ивановской области ', 'Управление МВД России по Калужской области ',
          'Управление МВД России по Костромской области ', 'Управление МВД России по Курской области ',
          'Управление МВД России по Липецкой области ', 'Главное управление МВД России по Московской области ',
          'Управление МВД России по Орловской области ', 'Управление МВД России по Рязанской области ',
          'Управление МВД России по Смоленской области ', 'Управление МВД России по Тамбовской области ',
          'Управление МВД России по Тверской области ', 'Управление МВД России по Тульской области ',
          'Управление МВД России по Ярославской области ', 'Главное управление МВД России по г. Москве ',
          'МВД по Республике Адыгея ', 'МВД по Республике Калмыкия ',
          'Главное управление МВД России по Краснодарскому краю ', 'Управление МВД России по Астраханской области ',
          'Главное управление МВД России по Волгоградской области ',
          'Главное управление МВД России по Ростовской области ', 'МВД по Республике Крым ',
          'Управление МВД России по г. Севастополю ', 'МВД по Республике Карелия ', 'МВД по Республике Коми ',
          'Управление МВД России по Архангельской области ', 'Управление МВД России по Вологодской области ',
          'Управление МВД России по Калининградской области ',
          'Главное управление МВД России по Санкт-Петербургу и Ленинградской области ',
          'Управление МВД России по Мурманской области ', 'Управление МВД России по Новгородской области ',
          'Управление МВД России по Псковской области ', 'Управление МВД России по Ненецкому автономному округу ',
          'МВД по Республике Бурятия ', 'МВД по Республике Саха (Якутия) ',
          'Управление МВД России по Приморскому краю ', 'Управление МВД России по Хабаровскому краю ',
          'Управление МВД России по Амурской области ', 'Управление МВД России по Камчатскому краю ',
          'Управление МВД России по Магаданской области ', 'Управление МВД России по Сахалинской области ',
          'Управление МВД России по Забайкальскому краю ', 'Управление МВД России по Еврейской автономной области ',
          'Управление МВД России по Чукотскому автономному округу ', 'МВД по Республике Алтай ',
          'МВД по Республике Тыва ', 'МВД по Республике Хакасия  ', 'Главное управление МВД России по Алтайскому краю ',
          'Главное управление МВД России по Красноярскому краю ', 'Главное управление МВД России по Иркутской области ',
          'Главное управление МВД России по Кемеровской области ',
          'Главное управление МВД России по Новосибирской области ', 'Управление МВД России по Омской области ',
          'Управление МВД России по Томской области ', 'Управление МВД России по Курганской области ',
          'Главное управление МВД России по Свердловской области ', 'Управление МВД России по Тюменской области ',
          'Главное управление МВД России по Челябинской области ',
          'Управление МВД России по Ханты-Мансийскому автономному округу - Югре ',
          'Управление МВД России по Ямало-Ненецкому автономному округу ', 'МВД по Республике Башкортостан  ',
          'МВД по Республике Марий Эл  ', 'МВД по Республике Мордовия ', 'МВД по Республике Татарстан  ',
          'МВД по Удмуртской Республике ', 'МВД по Чувашской Республике ',
          'Управление МВД России по Кировской области ', 'Главное управление МВД России по Нижегородской области ',
          'Управление МВД России по Оренбургской области ', 'Управление МВД России по Пензенской области ',
          'Главное управление МВД России по Пермскому краю ', 'Главное управление МВД России по Самарской области ',
          'Главное управление МВД России по Саратовской области ', 'Управление МВД России по Ульяновской области ',
          'Главное управление МВД России по Северо-Кавказскому федеральному округу ', 'МВД по Республике Дагестан ',
          'МВД по Республике Ингушетия ', 'МВД по Кабардино-Балкарской Республике ',
          'МВД по Карачаево-Черкесской Республике ', 'МВД по Республике Северная Осетия – Алания ',
          'Главное управление МВД России по Ставропольскому краю ', 'МВД по Чеченской Республике ']

english_words = ['area', 'book', 'business', 'case', 'child', 'company', 'country', 'day', 'eye', 'fact', 'family',
                'government', 'group', 'hand', 'home', 'job', 'life', 'lot', 'man', 'money', 'month', 'mother', 'Mr',
                'night', 'number', 'part', 'people', 'place', 'point', 'problem', 'program', 'question', 'right',
                'room', 'school', 'state', 'story', 'student', 'study', 'system', 'thing', 'time', 'water', 'way',
                'week', 'woman', 'word', 'work', 'world', 'year']

punctuation_marks = ['.', '_', '', '-']
mail_hostings = ['gmail.com', 'icloud.com', 'mail.ru', 'yandex.ru', 'yahoo.com', 'bk.ru', 'list.ru', 'inbox.ru',
                'rambler.ru']

date = datetime.now()

def email_generator():
    if random.choice(list(range(0, 2))):
        email = str(
            f"{random.choice(english_words)}{random.choice(punctuation_marks)}{random.choice(english_words)}@{random.choice(mail_hostings)}")
        return email
    else:
        email = str(
            f"{random.choice(english_words)}{random.choice(punctuation_marks)}{random.choice(english_words)}{random.choice(yearOfBirth)}@{random.choice(mail_hostings)}")
        return email

def phone_number_generator():
    phone_number = ['8', '-', '9']
    numbers = 11

    while numbers >= 0:
        if numbers == 9 or numbers == 5 or numbers == 2:
            phone_number.append('-')
            numbers -= 1
            continue
        phone_number.append(str(random.choice(phoneNumbers)))
        numbers -= 1

    result = ''.join(phone_number)

    return result

def name_generator():
    name_list = RussianNames().get_person().split()
    name_list[0], name_list[1], name_list[2] = name_list[2], name_list[0], name_list[1]
    name = (' '.join(name_list))
    return name

def client_generator(x):
    file = open(f'/home/let/Документы/PassGen/clients.txt', "at")

    while x > 0:
        file.write(str(
            f" {name_generator()}\n "
            f" Телефон: {phone_number_generator()}\n "
            f" Электронная почта: {email_generator()}\n "
            f" Дата рождения: {random.choice(day)}.{random.choice(month)}.{random.choice(yearOfBirth)}\n "
            f" Место рождения: РОССИЯ гор. {random.choice(cities)}\n "
            f" Паспорт: {random.choice(passportSeries)} {random.choice(passportNumbers)}\n "
            f" Код подразделения: {random.choice(departmentCode)}-{random.choice(departmentCode)}\n "
            f" Выдан: {random.choice(issued)}\n "
            f" Дата выдачи: {random.choice(day)}.{random.choice(month)}.{random.choice(yearOfIssue)}\n "
            f" Адресс: гор. {random.choice(cities)}, ул. {random.choice(streets)}, дом {random.choice(houseApartmentNumbers)}, кв. {random.choice(houseApartmentNumbers)}\n\n"))
        x -= 1

    file.close()
    print(f"Создан файл {file}")

def start():
    x = int(input("Сколько данных нужно сгенерировать?"))
    if x >= 1:
        client_generator(x)
    else:
        print(f"{x} - это не цифра. Попробуйте снова.")
        start()

start()