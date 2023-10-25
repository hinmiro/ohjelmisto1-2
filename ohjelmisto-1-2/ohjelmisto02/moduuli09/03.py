class Car:

    def __init__(self, plate, top_speed, current_speed=0, travelled=0):
        self.current_speed = current_speed
        self.travelled = travelled
        self.plate = plate
        self.top_speed = top_speed
        print(f"license: {self.plate}\ntopspeed: {self.top_speed}")
        print(f"current speed: {self.current_speed} km/h\ntraveled: {self.travelled} km")

    def accelerate(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.top_speed:
            self.current_speed = self.top_speed
        print(f"\nYour current speed is now {self.current_speed} km/h")

    def travel(self, hours):
        self.travelled += self.current_speed * hours
        print(f"\nYour current traveled distance is now {int(self.travelled)} km.")


car = Car("ABC-123", 142)

car.traveled = 2000
car.accelerate(60)
car.travel(1.5)
