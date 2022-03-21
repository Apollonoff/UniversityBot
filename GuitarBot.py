print("Здравствуйте! Как я могу к вам обращаться?")
name = input("Введите свое имя: ")
print(f"Здравствуйте, {name}! Это бот по рекомендации гитары по Вашим предпочтениям!")
print("Чат-бот базируется на рейтингах магазина Музторг\n")
print("Какую музыку Вы больше предпочитаете?")


print("Введите номера жанров в указанном списке\n"
      "1.Джаз\n"
      "2.Классика\n"
      "3.Рок\n"
      "4.Альтернатива\n"
      "5.Метал\n"
      "6.Блюз\n"
      "7.Кантри и блюграсс")

# пользователь вводит свои любимые жанры
likes = []  # массив выбранных предметов
while True:
    try:
        print("Введите номер и нажмите Enter...")
        print("Если хотите остановить ввод - введите 0")
        element = int(input())
        if element != 0:
            likes.append(element)
            if element > 7 or element < 0:
                print(f'{name}, введите только доступные варианты. Повторите снова')
                likes.remove(element)  # убираем из массива бракованный элемент
        else:
            print("Отличный выбор!")
            break
    except ValueError:  # ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
        print(f'{name}, введите только доступные варианты. Повторите снова')

likes_set = set(likes)  # перегоняем массив в множество
# # множество помогает избежать повторяющихся элементов3


# укрупненные сочения жанров по типу гитары
classic_set = {1, 2}
acoustic_set = {6, 7}
electro_set = {3, 4, 5, 6}

if likes_set.issubset(classic_set):
    print("Поздравляю, Вам подходит классическая гитара!")
    print("Назовите свой уровень игры на гитаре\n"
          "Выберите один вариант из списка:\n"
          "1. Начальный уровень\n"
          "2. Средний уровень\n"
          "3.Высокий уровень")
    sector_classic = 0
    while sector_classic < 1 or sector_classic > 3:
        try:
            sector_classic = int(input("Введите номер:"))
            if sector_classic < 1 or sector_classic > 3:
                print('Введите только доступные варианты. Повторите снова')
        except ValueError:  # ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
            print(f'{name}, введите только доступные варианты. Повторите снова')
    if sector_classic == 1:
        print("Вы только начинаете изучать базовые аккорды и у Вас все еще только впереди!\n"
              "Вот список гитар, которые идеально Вам подойдут:\n"
              "1.PRADO HS - 3805\n"
              "2.BELUCCI BC3805 SB\n"
              "3.ELITARO EL39 N\n"
              "4.ROCKDALE CLASSIC LIFE SB\n"
              "5.FABIO FB3410 BLS")
    elif sector_classic == 2:
        print("Вы уже успели серьезно изучить игру на гитаре и хотите инструмент, позволяющий сыграть все, что Вашей душе угодно!\n"
              "Вот список гитар, которые идеально Вам подойдут:\n"
              "1.ROCKDALE MODERN CLASSIC 100-SB\n"
              "2.FENDER ESC-105 CLASSIC\n"
              "3.CORT CLASSIC SERIES\n"
              "4.FLIGHT C-120 NA 1/2\n"
              "5.BARCELONA CG36BK 3/4")
    elif sector_classic == 3:
        print("Вы настоящий гуру игры на классической гитаре и хотите достойный инструмент!\n"
              "Вот список гитар, которые идеально Вам подойдут:\n"
              "1.FENDER CN-60S NYLON BLACK\n"
              "2.YAMAHA CG122MS\n"
              "3.CORDOBA IBERIA C5 CD\n"
              "4.PEREZ 610 CEDAR\n"
              "5.LAG GLA OC70")
if acoustic_set.issubset(likes_set):
    print("Поздравляю, Вам подходит акустическая гитара!")
    print("Назовите свой уровень игры на гитаре\n"
          "Выберите один вариант из списка:\n"
          "1. Начальный уровень\n"
          "2. Средний уровень\n"
          "3.Высокий уровень")
    sector_acoustic = 0
    while sector_acoustic < 1 or sector_acoustic > 3:
        try:
            sector_acoustic = int(input("Введите номер:"))
            if sector_acoustic < 1 or sector_acoustic > 3:
                print('Введите только доступные варианты. Повторите снова')
        except ValueError:  # ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
            print(f'{name}, введите только доступные варианты. Повторите снова')
    if sector_acoustic == 1:
        print("Вы только начинаете изучать базовые аккорды и у Вас все еще только впереди!\n"
              "Вот список гитар, которые идеально Вам подойдут:\n"
              "1.PRADO HS - 3807 / NA\n"
              "2.BELUCCI BC3820 RDS\n"
              "3.TERRIS TF-3802A NA\n"
              "4.COLOMBO LF - 3801 / BK\n"
              "5.ELITARO E4020 VTS")
    elif sector_acoustic == 2:
        print("Вы уже успели серьезно изучить игру на гитаре и хотите инструмент, позволяющий сыграть все, что Вашей душе угодно!\n"
              "Вот список гитар, которые идеально Вам подойдут:\n"
              "1.COLOMBO LF - 3800 / BK\n"
              "2.COLOMBO LF - 401 CEQ / N\n"
              "3.MARTINEZ FAW - 701\n"
              "4.FENDER FA-125 SUNBURST\n"
              "5.CORT AD810-OP STANDARD")
    elif sector_acoustic == 3:
        print("Вы настоящий гуру игры на акустической гитаре и хотите достойный инструмент!\n"
              "Вот список гитар, которые идеально Вам подойдут:\n"
              "1.FENDER CD-60SCE NATURAL\n"
              "2.LAVA ME 2 ACOUSTIC BLACK\n"
              "3.IBANEZ TCM50-GBO TALMANT\n"
              "4.FENDER CC-60SCE BLACK\n"
              "5.YAMAHA FG800M NATURAL")

if electro_set.issubset(likes_set):
    print("Поздравляю, Вам подходит электрогитара!")
    print("Назовите свой уровень игры на гитаре\n"
          "Выберите один вариант из списка:\n"
          "1. Начальный уровень\n"
          "2. Средний уровень\n"
          "3.Высокий уровень")
    sector_electro = 0
    while sector_electro < 1 or sector_electro > 3:
        try:
            sector_electro = int(input("Введите номер:"))
            if sector_electro < 1 or sector_electro > 3:
                print('Введите только доступные варианты. Повторите снова')
        except ValueError:  # ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
            print(f'{name}, введите только доступные варианты. Повторите снова')
    if sector_electro == 1:
        print("Вы только начинаете изучать базовые аккорды и у Вас все еще только впереди!\n"
              "Вот список гитар, которые идеально Вам подойдут:\n"
              "1.CORT G110-BK G SERIES\n"
              "2.JET JS-300 SB\n"
              "3.FENDER SQUIER MM STRATOCASTER BLACK\n"
              "4.IBANEZ GRX40-TFB\n"
              "5.CORT G110-SRD G SERIES")
    elif sector_electro == 2:
        print("Вы уже успели серьезно изучить игру на гитаре и хотите инструмент, позволяющий сыграть все, что Вашей душе угодно!\n"
              "Вот список гитар, которые идеально Вам подойдут:\n"
              "1.JACKSON JS1X DK MINION BLACK\n"
              "2.IBANEZ GIO GSA60-WNF WALNUT FLAT\n"
              "3.EPIPHONE Les Paul Standard 60s Iced Tea\n"
              "4.EPIPHONE LES PAUL STUDIO EBONY\n"
              "5.JACKSON JS22 DINKY DKA METALLIC BLUE")
    elif sector_electro == 3:
        print("Вы настоящий гуру игры на электрогитаре и хотите достойный инструмент!\n"
              "Вот список гитар, которые идеально Вам подойдут:\n"
              "1.FENDER PLAYER STRATOCASTER PF POLAR WHITE\n"
              "2.FENDER PLAYER PLUS STRAT HSS PF BELAIR BLUE\n"
              "3.IBANEZ RG8-WH 8-STRING RG\n"
              "4.GIBSON LES PAUL TRIBUTE SATIN TOBACCO BURSTK\n"
              "5.IBANEZ RG652AHMFX-NGB PRESTIGE")

#
# последнее сообщение от бота
print(f'{name}, спасибо, что воспользовались нашим ботом, желаем Вам удачи!')
