"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
её на экран.
"""

with open('task_5.txt', 'w+', encoding='utf-8') as x:
    print(' '.join([str(el) for el in range(1, 21)]), file=x)
    x.seek(0)
    print(sum(int(el) for el in x.read().split()))
