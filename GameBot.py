# приветствуем пользователя
print("Здравствуйте! Как я могу к вам обращаться?")
name = input("Введите свое имя: ")
print(f"Здравствуйте, {name}! Это бот показывает лучшую игру c 2000 по 2021!")
print("Чат-бот базируется на рейтингах сайта ITC.ua и The Game Awards\n")

# создадим обработчик ошибок
count_years = 0
while count_years < 1 or count_years > 7:  # защищаем от ввода некорректных цифр
    try:
        count_years = int(input('введите кол-во просматриваемых годов (<=22): '))
        if count_years < 1 or count_years > 7:
            print('Введите только доступные варианты. Повторите снова')
    except ValueError:  # ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
        print(f'{name}, введите только доступные варианты. Повторите снова')

print(f'\n{name}, введите года для просмотра лучших игр')
years = []  # массив выбранных годов
while len(years) != count_years:
    try:
        print("Введите номер и нажмите Enter...")
        element = int(input())
        years.append(element) # добавляем в массив год
        if element > 2021 or element < 2000: # убирает будущие или прошлые года
            print(f'{name}, введите только доступные варианты. Повторите снова')
            years.remove(element)  # убираем из массива бракованный элемент
        else:
            print("Год записан!")
    except ValueError:  # ValueError. Исключение, возникающее в случаях, когда в функцию передан аргумент с неподдерживаемым значением
        print(f'{name}, введите только доступные варианты. Повторите снова')

clear_years = list(set(sorted(years))) # сортирует years, удаляет повторяющиеся года и снова записывает в список clear_years

if 2000 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2000 год является Deus Ex!')

if 2001 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2001 год является Anachronox!')

if 2002 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2002 год является Warcraft III: Reign of Chaos!')

if 2003 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2003 год является TRON 2.0!')

if 2004 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2004 год является Vampire: The Masquerade – Bloodlines!')

if 2005 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2005 год является F.E.A.R.!')

if 2006 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2006 год является The Elder Scrolls IV: Oblivion!')

if 2007 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2007 год является The Witcher!')

if 2008 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2008 год является Fallout 3!')

if 2009 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2009 год является Call of Duty: Modern Warfare 2!')

if 2010 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2010 год является Red Dead Redemption!')

if 2011 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2011 год является The Elder Scrolls V: Skyrim!')

if 2012 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2012 год является The Walking Dead!')

if 2013 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2013 год является The Last of Us')

if 2014 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2014 год является Dragon Age: Inquisition!')

if 2015 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2015 год является The Witcher 3: Wild Hunt!')

if 2016 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2016 год является Overwatch!')

if 2017 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2017 год является Horizon Zero Dawn!')

if 2018 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2018 год является God of War!')

if 2019 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2019 год является Disco Elysium!')

if 2020 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2020 год является The Last of Us Part II!')

if 2021 in clear_years: # проверяем год игры в списке
    print(f'\n{name}, лучшей игрой за 2021 год является It Takes Two!')

