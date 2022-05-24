"""4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат."""


class Car:
    speed = 0
    color = 'black'
    name = 'Car'
    is_police = False

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}!!!')

    def go(self):
        self.speed = 50
        print('the car went!!!')

    def stop(self):
        self.speed = 0
        print('STOP!!!')

    def turn(self, direction: str):
        self.direction = direction
        print(f'A Car Turn {self.direction}!!!')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание скорость больше 60, а именно {self.speed}')
        else:
            print(f'Текущая скорость автомобиля {self.speed}!!!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание скорость больше 40, а именно {self.speed}')
        else:
            print(f'Текущая скорость автомобиля {self.speed}!!!')


class PoliceCar(Car):
    is_police = True


a = Car()
b = TownCar()
c = SportCar()
d = WorkCar()
k = PoliceCar()
print(1)
