class Car:
    current_speed = 0
    traveled = 0

    def __init__(self, plate, top_speed):
        self.plate = plate
        self.top_speed = top_speed
        print(f"license: {self.plate}\ntopspeed: {self.top_speed}")
        print(f"current speed: {self.current_speed} km/h\ntraveled: {self.traveled} km")

    def accelerate(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.top_speed:
            self.current_speed = self.top_speed
        print(f"Your current speed is now {self.current_speed} km/h")




car = Car("ABC-123", 142)

car.accelerate(+30)
car.accelerate(+70)
car.accelerate(+50)
car.accelerate(-200)
