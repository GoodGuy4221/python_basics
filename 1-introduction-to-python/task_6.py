"""6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
километров. Каждый день спортсмен увеличивал результат на 10% относительно
предыдущего. Требуется определить номер дня, на который результат спортсмена составит
не менее b километров. Программа должна принимать значения параметров a и b и выводить
одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
"""

result_first_day = float(input('Результат в первый день\n'))

desired_result = float(input('Желаемый результат\n'))

a = result_first_day

b = desired_result

count_day = 1

print(f'{count_day}-й день: {a}')

while a <= b:
    count_day += 1
    percent = (a / 100) * 10
    a = a + percent
    print(f'{count_day}-й день: {a:.2f}')
else:
    print(f'Ответ: на {count_day}-й день спортсмен достиг результата — не менее {int(desired_result)} км.')
