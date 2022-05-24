"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
"""


# def my_func(a, b, c):
#     my_list = [a, b, c]
#     my_list.remove(min(a, b, c))
#
#     return sum(my_list)


def my_func(a, b, c):
    if a == min(a, b, c):
        return b + c
    elif b == min(a, b, c):
        return a + c
    elif c == min(a, b, c):
        return a + b
    else:
        return a + b + c


print(my_func(51, 21, 94))
