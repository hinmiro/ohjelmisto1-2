import random


class Car:
    current_speed = 0
    traveled = 0

    def __init__(self, plate, top_speed):
        self.plate = plate
        self.top_speed = top_speed
        print(f"license: {self.plate}\ntopspeed: {self.top_speed}")
        print(f"current speed: {self.current_speed} km/h\ntraveled: {self.traveled} km\n")

    def accelerate(self, speed_change):
        self.current_speed += self.current_speed + speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.top_speed:
            self.current_speed = self.top_speed

    def travel(self, hours):
        self.traveled += self.current_speed * hours


temp = 1
cars = []
cars_order = []
for i in range(10):
    topspeed = random.randint(100, 200)
    car = Car(f"ABC-{temp}", topspeed)
    cars.append(car)
    temp += 1

while not any(car.traveled >= 10000 for car in cars):
    for car in cars:
        accelerate = random.randint(-10, 15)
        car.accelerate(accelerate)
        car.travel(1)

cars_order = sorted(cars, key=lambda x: x.traveled, reverse=True)

print(cars)
