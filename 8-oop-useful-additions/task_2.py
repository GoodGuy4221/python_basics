"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnErrorDivisionByZero(Exception):
    def __init__(self, message):
        self.message = message


dividend = input('введите делимое: ')
divider = input('введите делитель: ')

try:
    dividend = float(dividend)
    divider = float(divider)

    if divider == 0:
        raise OwnErrorDivisionByZero('Just Not Zero!!!')

    result = dividend / divider

except (ValueError, OwnErrorDivisionByZero) as error:
    print(error)
else:
    print(result)
finally:
    print('Ой все!!!')
