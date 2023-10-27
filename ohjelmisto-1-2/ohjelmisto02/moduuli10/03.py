class House:
    elevators = []

    def __init__(self, bottom, top, elevs):
        self.bottom = bottom
        self.top = top
        self.elevs = elevs

        for i in range(elevs):
            elev = Elevator(self.bottom, self.top)
            self.elevators.append(elev)

    def use_elevator(self, elevator_number, floor):
        print(f"Elevator {elevator_number + 1} starting to move floor {floor}.")
        self.elevators[elevator_number - 1].siirry_kerrokseen(floor)

    def firealarm(self):
        print("Fire alarm turned on!! All elevators are going to bottom floor.")
        for i in range(0, len(self.elevators)):
            house1.use_elevator(i, 0)


class Elevator:

    def __init__(self, bottom, top, current=0):
        self.bottom = bottom
        self.top = top
        self.current = current

    def siirry_kerrokseen(self, floor):
        if floor > self.current:
            for i in range(floor - self.current):
                self.kerros_ylos()
        elif floor < self.current:
            for i in range(self.current - floor):
                self.kerros_alas()

    def kerros_ylos(self):
        if self.current < self.top:
            self.current += 1
            print(f"You are now in floor {self.current}.")
        else:
            print("You are at top floor, cannot go higher.")

    def kerros_alas(self):
        if self.current >= self.bottom:
            self.current -= 1
            print(f"You are now in floor {self.current}.")
        else:
            print("You are at bottom floor, cannot go lower.")


house1 = House(1, 6, 2)
house1.use_elevator(1, 4)
print("**********")
house1.use_elevator(2, 3)
print("**********")
house1.use_elevator(1, 2)
print("**********")
house1.firealarm()
