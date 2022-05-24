"""4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number_n = int(input('Yor number\n'))

n = 0
a = 0

while not number_n == 0:
    n = number_n % 10
    if n > a:
        a = n
    number_n //= 10
else:
    print(a)
