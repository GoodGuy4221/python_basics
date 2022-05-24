"""7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

with open('task_7.txt', 'r', encoding='utf-8') as s:
    my_list = [{el.split()[0]: int(el.split()[2]) - int(el.split()[3]) for el in s}]
    ap = {'average_profit': int(
        sum([el for el in my_list[0].values() if not el < 0]) / len([el for el in my_list[0].values() if el > 0]))}
    my_list.append(ap)
    print(my_list)

with open('task_7_wr.txt', 'w', encoding='utf-8') as l:
    json.dump(my_list, l, ensure_ascii=False, indent=4)
