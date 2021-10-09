
class Car:
    def __init__(cls, speed, colour, name, is_police=False):
        cls.speed = speed
        cls.colour = colour
        cls.name = name
        cls.is_police = is_police

    def go(self):
        print(f'{self.name} rides')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print(f'Current speed {self.speed}')

    def params(self):
        param = f'Car brand: {self.name}, Car colour: {self.colour}'
        if self.is_police:
            param = f"{param}. It's a sound of da police!"
        print(param)

    def change_speed(cls, new_speed):
        cls.speed = new_speed


class TownCar(Car):
    def __init__(cls, speed, colour, name):
        super().__init__(speed, colour, name)
        if speed > 60:
            print('\nSpeed exceeded!\n')


class SportCar(Car):
    def __init__(cls, speed, colour, name):
        super().__init__(speed, colour, name)


class WorkCar(Car):
    def __init__(cls, speed, colour, name):
        super().__init__(speed, colour, name)
        if speed > 40:
            print('\nSpeed exceeded!\n')


class PoliceCar(Car):
    def __init__(cls, speed, colour, name, is_police=True):
        super().__init__(speed, colour, name, is_police)


print('-' * 100)

person_car = TownCar(70, 'Red', 'Toyota')
person_car.go()
person_car.turn('left')
person_car.show_speed()
person_car.change_speed(50)
person_car.go()
person_car.turn('right')
person_car.show_speed()
person_car.stop()
person_car.params()

print('-' * 100)

worker_car = WorkCar(50, 'Black', 'Ford')
worker_car.go()
worker_car.turn('left')
worker_car.stop()
worker_car.params()

print('-' * 100)

police_car = PoliceCar(90, 'Blue-White', 'Mustang')
police_car.go()
police_car.turn('drift')
police_car.stop()
police_car.params()

print('-' * 100)

sport_car = SportCar(120, 'Red', 'Ferrari')
sport_car.go()
sport_car.turn('right drift')
sport_car.stop()
sport_car.params()
