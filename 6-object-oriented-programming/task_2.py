"""2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    _length = 20
    _width = 5000

    def __init__(self, mass, asphalt_thickness):
        self.mass = mass
        self.asphalt_thickness = asphalt_thickness

    def my(self):
        mass = self.mass
        asphalt_thickness = self.asphalt_thickness
        _length = Road._length
        _width = Road._width
        self.mass = mass
        self.asphalt_thickness = asphalt_thickness
        print(f'{int((_length * _width * mass * asphalt_thickness) / 1000)} т.')


a = Road(25, 5)
a.my()
