class Hissi:

    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.aloitus = 0

    def siirry_kerrokseen(self, kertaa):
        if kertaa < self.aloitus:
            for i in range(kertaa):
                hissi1.kerros_ylos()
        elif kertaa > self.aloitus:
            for i in range(kertaa):
                hissi1.kerros_alas()

    def kerros_ylos(self):
        self.aloitus += 1
        print(f"Ole")

    def kerros_alas(self):
        self.aloitus -= 1


hissi1 = Hissi(1, 10)
hissi1.siirry_kerrokseen(6)
