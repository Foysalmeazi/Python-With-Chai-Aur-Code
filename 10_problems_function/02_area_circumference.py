from math import pi

radius = int(input('Enter Radius:'))

def circle_stats (radius):
    area = round((pi * radius**2), 2)
    circumference = round((2*pi*radius), 2)

    return area, circumference

A,C = circle_stats (radius)

print(f'Ares: {A}, Circumference {C}')