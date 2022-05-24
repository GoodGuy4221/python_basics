"""6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

words = input('В программу должна попадать строка из слов, разделенных пробелом.\n').split()


def int_func(words):
    words = ' '.join(words)
    return words.title()


print(int_func(words))
