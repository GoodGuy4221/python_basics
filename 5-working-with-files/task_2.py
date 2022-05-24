"""2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""

with open('task_2.txt', 'r', encoding='utf-8') as text:
    for i, el in enumerate(text.readlines(), 1):
        print(f'В {i} строке {len(el.split())} слов(а)')
