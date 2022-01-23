# name_User1 = input("Введите ваше имя: ")
# mark1 = int(input(f"Приветствуем,{name_User1}! Пожалуйста, введите оценку магазина: "))
# name_User2 = input("Введите ваше имя: ")
# mark2 = int(input(f"Приветствуем,{name_User2}! Пожалуйста, введите оценку магазина: "))
# name_User3 = input("Введите ваше имя: ")
# mark3 = int(input(f"Приветствуем,{name_User3}! Пожалуйста, введите оценку магазина: "))
# name_User4 = input("Введите ваше имя: ")
# mark4 = int(input(f"Приветствуем,{name_User4}! Пожалуйста, введите оценку магазина: "))
#
# count_users = 4
#
# print(f"По опросам пользователей средняя оценка равна {(mark1+mark2+mark3+mark4)/count_users}.")
marks = '4444'
count_one = marks.count('1')
count_two = marks.count('2')
count_three = marks.count('3')
count_four = marks.count('4')
count_five = marks.count('5')
average_mark = (count_one+count_two*2+count_three*3+count_four*4+count_five*5)/len(marks)
# печать результата
print(f'Средняя оценка пользователей: {average_mark}')
print(f'Приближенная средняя оценка пользователей: {round(average_mark)}')