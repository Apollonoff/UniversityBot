# приветствуем пользователя
print("Привет! Как я могу к тебе обращаться?")
name = input("Введите свое имя: ")
print(f"Здравствуйте, {name}! Это бот показывает лучших исполнителей жанра музыки EDM!")
# print("Чат-бот базируется на рейтингах сайта Кинопоиск\n")

ans = True
while ans:
    genres_count = 0
    while genres_count < 1 or genres_count > 9:  # защищаем от ввода некорректных цифр
        try:
            genres_count = int(input('Введите кол-во любимых жанров (<=9): '))
            if genres_count < 1 or genres_count > 9:
                print('Введите только доступные варианты. Повторите снова')
        except ValueError:  # ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
            print(f'{name}, введите только доступные варианты. Повторите снова')

    print("Введите номера жанров в указанном списке:\n"
          "1.Deep House\n"
          "2.Techno\n"
          "3.Rave\n"
          "4.Trance\n"
          "5.Drum and Bass\n"
          "6.Dubstep\n"
          "7.Trap\n"
          "8.Bass House\n"
          "9.Future Bass")

    # пользователь вводит свои любимые жанры

    likes = []  # массив выбранных предметов
    while len(likes) != genres_count:
        try:
            print("Введите номер и нажмите Enter...")
            element = int(input())
            likes.append(element)
            if element > 9 or element < 1:
                print(f'{name}, можно ввести только доступные варианты. Повторите снова')
                likes.remove(element)  # убираем из массива бракованный элемент
            else:
                print("Отличный выбор!")
        except ValueError:  # ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
            print(f'{name}, можно ввести только доступные варианты. Повторите снова')

    if 1 in likes:  #проверяем жанр в списке
        print(f'\n{name}, вот список лучших исполнителей в жанре Deep House:\n'
              '1.Diplo\n'
              '2.Стив Аоки\n'
              '3.Давид Гетта\n'
              '4.Swedish House Mafia\n'
              '5.Zedd\n')
    if 2 in likes:
        print(f'\n{name}, вот список лучших исполнителей в жанре Techno:\n'
              '1.Prodigy\n'
              '2.Gesaffelstein\n'
              '3.Пол ван Дайк\n'
              '4.Tiesto\n'
              '5.Бенни Бенасси\n')
    if 3 in likes:
        print(f'\n{name}, вот список лучших исполнителей в жанре Rave:\n'
              '1.The Prodigy\n'
              '2.Die Antwoord\n'
              '3.Scooter\n'
              '4.Little Big\n'
              '5.GSPD\n')
    if 4 in likes:
        print(f'\n{name}, вот список лучших исполнителей в жанре Trance:\n'
              '1.Armin van Buuren\n'
              '2.ATB\n'
              '3.Tiësto\n'
              '4.Paul van Dyk\n'
              '5.Paul Oakenfold')
    if 5 in likes:
        print(f'\n{name}, вот список лучших исполнителей в жанре Drum and Bass:\n'
              '1.Noisia\n'
              '2.Feint\n'
              '3.Chase & Status\n'
              '4.High Contrast\n'
              '5.London Elektricity\n')
    if 6 in likes:
        print(f'\n{name}, вот список лучших исполнителей в жанре Dubstep:\n'
              '1.Burial\n'
              '2.Skrillex\n'
              '3.Skream\n'
              '4.Nero\n'
              '5.Benga\n')
    if 7 in likes:
        print(f'\n{name}, вот список лучших исполнителей в жанре Trap:\n'
              '1.DJ Snake\n'
              '2.Dropzone\n'
              '3.Elliphant\n'
              '4.Zara Larsson\n'
              '5.The Chainsmokers\n')
    if 8 in likes:
        print(f'\n{name}, вот список лучших исполнителей в жанре Bass House:\n'
              '1.Joyryde\n'
              '2.Ibranovski\n'
              '3.Habstrakt\n'
              '4.Valentino Khan\n'
              '5.Moonboy\n')
    if 9 in likes:
        print(f'\n{name},вот список лучших исполнителей в жанре Future Bass:\n'
              '1.Flume\n'
              '2.Marshmello\n'
              '3.San Holo\n'
              '4.Kaytranada\n'
              '5.Troyboi\n')
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

