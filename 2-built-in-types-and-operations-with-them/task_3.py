"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
"""

# month = int(input('Введите номер месяца\n'))
#
# list_month = ['зима', 'весна', 'лето', 'осень',]
#
# month = month // 3 % 4
#
# print(list_month[month])
month = 'None'
while not month.isdecimal():
    month = input('Введите номер месяца\n')
    # if month.isdigit():
    #     break
else:
    month = int(month)

# try:
#     month = int(month)
# except TypeError:
#     print('Вы ввели что-то не то, TypeError')
# except ValueError:
#     print('Вы ввели что-то не то, ValueError')


dict_month = {0: 'зима',
              1: 'весна',
              2: 'лето',
              3: 'осень', }

month = month // 3 % 4

print(dict_month[month])
