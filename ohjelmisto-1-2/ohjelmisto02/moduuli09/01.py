class Car:

    def __init__(self, plate, top_speed, current_speed=0, travelled=0):
        self.current_speed = current_speed
        self.travelled = travelled
        self.plate = plate
        self.top_speed = top_speed
        print(f"license: {self.plate}\ntopspeed: {self.top_speed}")
        print(f"current speed: {current_speed} km/h\ntraveled: {travelled} km")


car = Car("ABC-123", 142)
