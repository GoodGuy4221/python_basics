"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
время выполнения расчёта для конкретных значений необходимо запускать скрипт с
параметрами.
"""

from sys import argv

name, output_in_hours, rate_per_hour, the_prize = argv


def salary(output_in_hours, rate_per_hour, the_prize):
    return (float(output_in_hours) * float(rate_per_hour)) + float(the_prize)


print(salary(output_in_hours, rate_per_hour, the_prize))
