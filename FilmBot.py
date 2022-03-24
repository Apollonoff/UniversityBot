# приветствуем пользователя
print("Здравствуйте! Как я могу к вам обращаться?")
name = input("Введите свое имя: ")
print(f"Здравствуйте, {name}! Это бот показывает топ фильмов по жанрам!")
print("Чат-бот базируется на рейтингах сайта Кинопоиск\n")

ans = True #обеспечивает многократное использование бота
while ans:
    genres_count = 0
    while genres_count < 1 or genres_count > 9:  # защищаем от ввода некорректных цифр
        try:
            genres_count = int(input('введите кол-во любимых жанров (<=9): '))
            if genres_count < 1 or genres_count > 9:
                print('Введите только доступные варианты. Повторите снова')
        except ValueError:  # ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
            print(f'{name}, введите только доступные варианты. Повторите снова')

    print("Введите номера жанров в указанном списке\n"
          "1.Боевик\n"
          "2.Детектив\n"
          "3.Документальный\n"
          "4.Драма\n"
          "5.Комедия\n"
          "6.Приключения\n"
          "7.Ужасы\n"
          "8.Фантастика\n"
          "9.Мультфильмы")

    # пользователь вводит свои любимые жанры

    likes = []  # массив выбранных предметов

    while len(likes) != genres_count:
        try:
            print("Введите номер и нажмите Enter...")
            element = int(input())
            likes.append(element)
            if element > 9 or element < 1:
                print(f'{name}, введите только доступные варианты. Повторите снова')
                likes.remove(element)  # убираем из массива бракованный элемент
            else:
                print("Отличный выбор!")
        except ValueError:  # ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
            print(f'{name}, введите только доступные варианты. Повторите снова')

    if 1 in likes:  #проверяем жанр в списке
        print(f'\n{name}, вот список лучших боевиков:\n'
              '1.Леон\n'
              '2.Карты, деньги, два ствола\n'
              '3.Брат 2 (2000)\n'
              '4.Шерлок Холмс\n'
              '5.Троя\n')
    if 2 in likes:
        print(f'\n{name}, вот список лучших детективов:\n'
              '1.Приключения Шерлока Холмса и доктора Ватсона: Собака Баскервилей (ТВ, 1981)\n'
              '2.Шестое чувство\n'
              '3.Ищите женщину\n'
              '4.Ошибка резидента\n'
              '5.Достать ножи\n')
    if 3 in likes:
        print(f'\n{name}, вот список лучших документальных фильмов:\n'
              '1.Земляне\n'
              '2.Земля: Один потрясяющий день\n'
              '3.Медведи Камчатки. Начало жизни\n'
              '4.Сенна\n'
              '5.Топ Гир: Идеальное путешествие\n')
    if 4 in likes:
        print(f'\n{name}, вот список лучших драм:\n'
              '1.Побег из Шоушенка\n'
              '2.Зеленая миля\n'
              '3.Форрест Гамп\n'
              '4.Список Шиндлера\n'
              '5.1+1')
    if 5 in likes:
        print(f'\n{name}, вот список лучших комедий:\n'
              '1.Иван Васильевич меняет профессию\n'
              '2.Джентельмены удачи\n'
              '3.Один дома\n'
              '4.Маска\n'
              '5.Отель "Гранд Будапешт"\n')
    if 6 in likes:
        print(f'\n{name}, вот список лучших приключенческих фильмов:\n'
              '1.Хороший, плохой злой\n'
              '2.Восточный ветер\n'
              '3.Индиана Джонс и последний крестовый поход (1989)\n'
              '4.Пираты Карибского моря: На краю света (2007)\n'
              '5.Выживший\n')
    if 7 in likes:
        print(f'\n{name}, вот список самых популярных фильмов ужасов:\n'
              '1.Чужой\n'
              '2.Чужие\n'
              '3.Другие\n'
              '4.Хищник\n'
              '5.От заката до рассвета\n')
    if 8 in likes:
        print(f'\n{name}, вот список лучших фантастических фильмов:\n'
              '1.Начало\n'
              '2.Назад в будущее\n'
              '3.Интерстеллар\n'
              '4.Темный рыцарь\n'
              '5.Матрица\n')
    if 9 in likes:
        print(f'\n{name}, вот список лучших мультфильмов:\n'
              '1.Король Лев\n'
              '2.Тайна Коко\n'
              '3.Душа\n'
              '4.ВАЛЛИ\n'
              '5.Зверополис\n')

    while True:
        print("Хотите узнать про еще какие-нибудь жанры? Введите Да или Нет")
        q = input()
        if q == 'Да' or q == "да" or q == "yes" or q == "Yes":
            break
        elif q == 'Нет' or q == "нет" or q == "No" or q == "no":
            ans = False
            break
        else:
            print("Введите допустимое значение...")


# последнее сообщение от бота
print(f'{name}, спасибо, что воспользовались нашим ботом, желаем Вам удачи!')

