"""3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open('task_3.txt', 'r', encoding='utf-8') as r:
    my_dict = {line.split()[0]: float(line.split()[1]) for line in r}
    print(f'Имеет оклад менее 20 тыс: { {el: str(round(e)) for el, e in my_dict.items() if e < 20000} }')
    sum = 0
    for e, el in enumerate(my_dict.values(), 1):
        sum += float(el)
    print(f'Подсчет средней величины дохода сотрудников: {round(sum / e, 2)}')

# with open('task_3.txt', 'r', encoding='utf-8') as r:
#     my_dict = {line.split()[0]: float(line.split()[1]) for line in r}
#     print(f'Подсчет средней величины дохода сотрудников: {round(sum(my_dict.values()) / len(my_dict), 3)}\n'
#     f'Имеет оклад менее 20 тыс: {[el[0] for el in my_dict.items() if el[1] < 20000]}')
