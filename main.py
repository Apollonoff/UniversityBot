#такую хуйню можно делать только за деньги
import collections

print("Здравствуйте! Как я могу к вам обращаться?")
name = input("Введите свое имя: ")
print(f"Здравствуйте, {name}! Это бот по рекомендации высшего учебного заведения по Вашим жизненным предпочтениям!")
print("Пожалуйста, введите те школьные предметы, по которым Вы собираетесь сдавать ЕГЭ!")
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
skills_list = list(input().split())
print(skills_list)
# базовые сочетания предметов
bsc_list1 = ['1', '2', '3']
bsc_list2 = ['7', '9', '10']

if collections.Counter(bsc_list1) == collections.Counter(skills_list):
      print('Поздравляю, Вы выбрали техническое направление!')
      print("Какая сфера технического образования Вам больше нравится?\n"
            "Выберите один вариант из списка..\n"
            "1. Инженерная сфера\n"
            "2. Сфера IT\n"
            "3. Сфера строительства\n"
            "4. Научная сфера")
      sector = int(input())
      if sector == 1:
            print("Прекрасно! Вот список лучших инженерных ВУЗов Москвы:\n"
                  "1. МГТУ им. Н. Э. Баумана\n"
                  "2.\n"
                  "3.\n")
      elif sector == 2:
            print("Прекрасно! Вот список лучших IT ВУЗов Москвы:\n"
                  "1. \n"
                  "2.\n"
                  "3.\n")
      elif sector == 3:
            print("Прекрасно! Вот список лучших строительных ВУЗов Москвы:\n"
                  "1. \n"
                  "2.\n"
                  "3.\n")
      else:
            print("Прекрасно! Вот список лучших ВУЗов Москвы:\n"
                  "1. \n"
                  "2.\n"
                  "3.\n")
if collections.Counter(bsc_list2) == collections.Counter(skills_list):
      print('Поздравляю, Вы выбрали гумманитарное направление!')