import time


class Auto:
    def __init__(self, brand, age, mark, color="", weight=""):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print("move")

    def birthday(self):
        self.age += 1
        print(self.age)

    def stop(self):
        print("stop")


bmw = Auto("BWM", 15, "e60")
bmw.move()
bmw.stop()
bmw.birthday()


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color="", weight=""):
        super().__init__(brand, age, mark, color="", weight="")
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


truck_volvo = Truck("volvo", 10, "FX", 10000)
truck_mercedes = Truck("mercedes", 5, "2000s", 15000)
truck_volvo.move()
truck_volvo.load()
truck_volvo.stop()
truck_volvo.birthday()
print(truck_volvo.brand)
print(truck_volvo.age)
print(truck_volvo.mark)
print(truck_volvo.max_load)

truck_mercedes.move()
truck_mercedes.load()
truck_mercedes.stop()
truck_mercedes.birthday()
print(truck_mercedes.brand)
print(truck_mercedes.age)
print(truck_mercedes.mark)
print(truck_mercedes.max_load)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color="", weight=""):
        super().__init__(brand, age, mark, color="", weight="")
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


car_audi = Car("audi", 7, "s8", 280)
car_bmw = Car("bmw", 3, "m5", 300)
car_audi.move()
car_audi.stop()
car_audi.birthday()
print(car_audi.brand)
print(car_audi.age)
print(car_audi.mark)

car_bmw.move()
car_bmw.stop()
car_bmw.birthday()
print(car_bmw.brand)
print(car_bmw.age)
print(car_bmw.mark)
