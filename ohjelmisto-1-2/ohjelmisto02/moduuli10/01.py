class Elevator:

    def __init__(self, bottom, top, current=0):
        self.bottom = bottom
        self.top = top
        self.current = current

    def siirry_kerrokseen(self, floor):
        if floor > self.current:
            for i in range(floor - self.current):
                elev1.kerros_ylos()
        elif floor < self.current:
            for i in range(self.current - floor):
                elev1.kerros_alas()

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


elev1 = Elevator(1, 10)
elev1.siirry_kerrokseen(6)
print("*********")
elev1.siirry_kerrokseen(4)
print("*********")
elev1.siirry_kerrokseen(6)
print("*********")
elev1.siirry_kerrokseen(10)
print("*********")
elev1.siirry_kerrokseen(11)
print("*********")
elev1.siirry_kerrokseen(0)
print("*********")
elev1.siirry_kerrokseen(-1)
