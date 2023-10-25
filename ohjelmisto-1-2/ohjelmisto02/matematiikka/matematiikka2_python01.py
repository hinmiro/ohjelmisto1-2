# TEHTÄVÄ 1

import numpy as np

a = 2.493
b = 0.911
c = 137.7
d = 62.3

print(f"\nTehtävä 1 a) {np.degrees(a):.3f} deg")
print(f"Tehtävä 1 b) {np.degrees(b):.3f} deg")
print(f"\nTehtävä 2 a) {np.radians(c):.3f} rad")
print(f"Tehtävä 2 b) {np.radians(d):.3f} rad")

A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
print("-----------------------------------------")
print("Tehtävä 3\n")

for i in A:
    print(f"{np.radians(i):.5f}")
