class Car:
    current_speed = 0
    traveled = 0

    def __init__(self, plate, top_speed):
        self.plate = plate
        self.top_speed = top_speed
        print(f"license: {self.plate}\ntopspeed: {self.top_speed}")
        print(f"current speed: {self.current_speed} km/h\ntraveled: {self.traveled} km")


car = Car("ABC-123", 142)
