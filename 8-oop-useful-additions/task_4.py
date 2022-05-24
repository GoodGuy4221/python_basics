"""4. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата"""


class ComplexNumber:
    def __init__(self, complex_number):
        self.complex_number = complex_number

    def __add__(self, other):
        return complex(self.complex_number + other.complex_number)

    def __mul__(self, other):
        return complex(self.complex_number * other.complex_number)


a = ComplexNumber(51)
b = ComplexNumber(21)
print(a + b)
print(a * b)
