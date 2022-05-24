"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

with open('task_4.txt', 'r', encoding='utf-8') as t:
    r = open('task_4_ru.txt', 'w', encoding='utf-8')
    for el in t:
        if el.split()[0] == 'One':
            r.write('Один ' + ' '.join(el.split()[1:]) + '\n')
        elif el.split()[0] == 'Two':
            r.write('Два ' + ' '.join(el.split()[1:]) + '\n')
        elif el.split()[0] == 'Three':
            r.write('Три ' + ' '.join(el.split()[1:]) + '\n')
        elif el.split()[0] == 'Four':
            r.write('Четыре ' + ' '.join(el.split()[1:]) + '\n')
    r.close()
