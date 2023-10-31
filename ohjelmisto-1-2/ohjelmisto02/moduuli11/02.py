class Car:

    def __init__(self, plate, top_speed, current_speed=0, travelled=0):
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.travelled = travelled
        self.plate = plate

    def travel(self, hours):
        self.travelled += self.top_speed * hours
        print(f"{self.plate} has {self.travelled}km in odometer")


class Ev(Car):

    def __init__(self, plate, top_speed, battery_capacity):
        super().__init__(plate, top_speed)
        self.battery_capacity = battery_capacity


class Icv(Car):

    def __init__(self, plate, top_speed, tank_capacity):
        super().__init__(plate, top_speed)
        self.tank_capacity = tank_capacity


cars = []

ev1 = Ev("ABC-123", 180, 52.5)
icv1 = Icv("ABC-113", 165, 32.3)

ev1.travel(3)
icv1.travel(3)
