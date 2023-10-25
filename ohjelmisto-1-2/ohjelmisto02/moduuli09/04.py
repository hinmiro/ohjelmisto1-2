import random


class Car:

    def __init__(self, plate, top_speed, current_speed=0, travelled=0):
        self.current_speed = current_speed
        self.travelled = travelled
        self.plate = plate
        self.top_speed = top_speed
        print(f"license: {self.plate}\ntopspeed: {self.top_speed}")
        print(f"current speed: {self.current_speed} km/h\ntravelled: {self.travelled} km\n")

    def accelerate(self, speed_change):
        self.current_speed += self.current_speed + speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.top_speed:
            self.current_speed = self.top_speed

    def travel(self, hours):
        self.travelled += self.current_speed * hours


temp = 1
cars = []
cars_order = []
for i in range(10):
    topspeed = random.randint(100, 200)
    car = Car(f"ABC-{temp}", topspeed)
    cars.append(car)
    temp += 1

while not any(car.travelled >= 10000 for car in cars):
    for car in cars:
        accelerate = random.randint(-10, 15)
        car.accelerate(accelerate)
        car.travel(1)

cars_order = sorted(cars, key=lambda x: x.travelled, reverse=True)

for car in cars_order:
    print(f"{car.plate} ----- {car.travelled}")
