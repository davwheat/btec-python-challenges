# Circle properties
# 3 points

import math


def PrintDetailsOfCircle(angle, diameter):
    # diameter / 2
    radius = diameter / 2
    # pi * r^2
    area = math.pi * (radius ** 2)
    # pi * d
    circumference = math.pi * diameter
    # pi * d * (degrees / 360)
    arcLength = math.pi * diameter * (angle / 360)

    # Output all data
    print(f"Arc angle: {angle}")
    print(f"Diameter: {diameter}")
    print(f"Circle area: {area}")
    print(f"Circle circumference: {circumference}")
    print(f"Arc length: {arcLength}")


PrintDetailsOfCircle(360, 25)
print("\n\n")
PrintDetailsOfCircle(180, 15)