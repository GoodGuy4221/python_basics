"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, сдекоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""

import time


class Date:
    def __init__(self, number, month, year):
        self.number = number
        self.month = month
        self.year = year

    @classmethod
    def date_int(cls, date):
        number, month, year = map(int, date.split('-'))
        return cls(number, month, year)

    @staticmethod
    def validation(obj):
        date = f'{obj.number}/{obj.month}/{obj.year}'
        try:
            valid_date = time.strptime(date, '%d/%m/%Y')
        except ValueError:
            return 'Invalid date!'
        else:
            return date


a = Date.date_int('21-09-1880')
print(Date.validation(a))
