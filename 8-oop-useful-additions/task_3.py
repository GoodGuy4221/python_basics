"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
пользователя данные и заполнять список необходимо только числами. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа
элемента. Вносить его в список, только если введено число. Класс-исключение должен не
позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться."""


class OwnErrorDivisionByZero(Exception):
    def __init__(self, alarm):
        self.alarm = alarm


my_list = []
while True:
    try:
        input_data = input('Введите новый элемент списка, только число или цифра или для выхода введите: stop.\n')
        if input_data == 'stop': break
        if not input_data.isdigit():
            raise OwnErrorDivisionByZero('Это не привести к числу или цифре!!!')
        else:
            my_list.append(float(input_data))
    except OwnErrorDivisionByZero as error:
        print(error)
    else:
        print('Попробуйте еще!!!')
    finally:
        print('*' * 12)

print(my_list)
