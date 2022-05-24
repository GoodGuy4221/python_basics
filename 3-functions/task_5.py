"""5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def five():
    numbers = ''
    list_int = []
    sum_int = 0
    while True:
        numbers = input('Программа запрашивает у пользователя строку чисел, разделенных пробелом:\n').split()
        if numbers == ['q']:
            print('finished')
            break
        if numbers.count('q') > 0:
            numbers.remove('q')
            for el in numbers:
                list_int.append(int(el))
            sum_int += sum(list_int)
            list_int = []
            print(sum_int)
            print('finished')
            break
        for el in numbers:
            list_int.append(int(el))
        sum_int += sum(list_int)
        list_int = []
        print(sum_int)


five()
