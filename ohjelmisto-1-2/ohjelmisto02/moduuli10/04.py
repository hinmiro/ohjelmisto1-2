import random


class Race:
    name = ""
    length = 0

    def __init__(self, name, length, cars):
        Race.name = name
        Race.length = length
        self.cars = cars

    def hour_goes(self):
        for i in self.cars:
            speed = random.randint(-10, 15)
            i.accelerate(speed)
            i.travel(1)

    def print_status(self):
        print("---Race status----")
        self.sort_cars = sorted(cars, key=lambda x: x.travelled, reverse=True)
        for car in self.sort_cars:
            print(" ----------------------------")
            print(f"| {car.plate}  |  {car.current_speed}   |  {car.travelled} |")

    def race_over(self):
        count = 1
        for i in cars:
            if i.travelled >= Race.length:
                print("")
                for i in self.sort_cars:
                    print(f"{count}. {i.plate}------{i.travelled}")
                    count += 1
                return True
            else:
                return False


class Car:

    def __init__(self, plate, top_speed, current_speed=0, travelled=0):
        self.current_speed = current_speed
        self.travelled = travelled
        self.plate = plate
        self.top_speed = top_speed

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
for i in range(10):
    topspeed = random.randint(100, 200)
    car = Car(f"ABC-{temp}", topspeed)
    cars.append(car)
    temp += 1

race1 = Race("Suuri romuralli", 8000, cars)

ten = 0
flag = False
while not flag:
    race1.hour_goes()
    flag = race1.race_over()
    ten += 1
    if ten == 10:
        ten = 0
        race1.print_status()
