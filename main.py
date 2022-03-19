import collections  # импортируем встроенный модуль Python

print("Здравствуйте! Как я могу к вам обращаться?")
name = input("Введите свое имя: ")
print(f"Здравствуйте, {name}! Это бот по рекомендации высшего учебного заведения по Вашим жизненным предпочтениям!")
print("Пожалуйста, введите те школьные предметы, по которым Вы собираетесь сдавать ЕГЭ!\n"
      "Чат-бот базируется на рейтингах агенства RAEX\n")
print("Введите через пробел номера предметов в указанном списке\n"
      "1.Математика профиль.\n"
      "2.Физика\n"
      "3.Информатика\n"
      "4.Литература\n"
      "5.География\n"
      "6.Химия\n"
      "7.История\n"
      "8.Биология\n"
      "9.Обществознание\n"
      "10.Английский\n"
      "11.Немецкий\n"
      "12.Испанский\n"
      "13.Французский\n")
# абитуриент вводит свои выбранные предметы
skills_list = set(input().split())  # разделяет предметы при помощи функции slpit() по пробелу и записывает в множество
# множество помогает избежать повторяющихся элементов
print(skills_list)
# укрупнённые сочетания предметов абитуриента по гуманитарным, техническим и химико-биологическим профилям
tech_set = {'1', '2', '3'}
gum_set = {'4', '7', '9', '10', '11', '12', '13'}

if skills_list.issubset(tech_set):  # проверяет, находятся ли предметы абитуры в укрупненном техническом множестве
    print('Поздравляю, Вы выбрали техническое направление!')
    print("Какая сфера технического образования Вам больше нравится?\n"
          "Выберите один вариант из списка..\n"
          "1. Инженерная сфера\n"
          "2. Сфера IT\n"
          "3. Сфера строительства\n"
          "4. Научная сфера\n"
          "5. Машиностроение и робототехника")
    sector = str
    while sector == str: #обработчик ошибок, нужен для перехвата некорректного ввода пользователем
        try:
            sector = int(input())
        except ValueError: #ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
            print(f'{name}, введите только доступные варианты. Повторите снова')
    while sector < 1 or sector > 5:  # защищаем от ввода некорректных цифр
        sector = int(input('пожалуйста, введите цифру от 1 до 5: '))
    if sector == 1:
        print("Прекрасно! ТОП 3 лучших инженерных ВУЗов:\n"
              "1.Московский государственный технический университет имени Н.Э. Баумана (национальный исследовательский университет)\n"
              "2.Московский физико-технический институт\n"
              "3.Национальный исследовательский ядерный университет «МИФИ»\n")
    elif sector == 2:
        print("Прекрасно! ТОП 3 лучших IT ВУЗов:\n"
              "1.Московский государственный университет имени М.В. Ломоносова \n"
              "2.Московский физико-технический институт (национальный исследовательский университет)\n"
              "3.Университет ИТМО\n")
    elif sector == 3:
        print("Прекрасно! ТОП 3 лучших строительных ВУЗов:\n"
              "1.Санкт-Петербургский государственный архитектурно-строительный университет \n"
              "2.Национальный исследовательский Московский государственный строительный университет\n"
              "3.Московский архитектурный институт (Государственная академия) – МАРХИ\n")
    elif sector == 4:
        print("Прекрасно! ТОП 3 лучших научных ВУЗов:\n"
              "1.Московский государственный университет имени М.В. Ломоносова \n"
              "2.Московский физико-технический институт (национальный исследовательский университет)\n"
              "3.Национальный исследовательский Томский государственный университет\n")
    elif sector == 5:
        print("Прекрасно! ТОП 3 лучших ВУЗов в сфере машиностроения и мехатроники:\n"
              "1.Московский государственный технический университет имени Н.Э. Баумана (национальный исследовательский университет)\n"
              "2.Университет ИТМО\n"
              "3.Томский политехнический университет\n")
if skills_list.issubset(gum_set):
    print('Поздравляю, Вы выбрали гуманитарное направление!')

# последнее сообщение от бота
print(f'{name}, спасибо, что воспользовались нашим ботом, желаем вам удачи!')
