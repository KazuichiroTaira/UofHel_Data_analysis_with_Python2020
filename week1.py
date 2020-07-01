
#print("Hello world2!")

#print("hello, " "Aurélien!", "How are you?")

#print(1,"plus", 2, "equals", 1+2)

#name = input("Give me your name: Jarkko")
#print("Hello,", name)

import math

def area_of_triangle(b, h):

    t = b * h * 1 / 2

    return f'The area is {t}'


def area_of_rectangle(b, h):

    r = b * h

    return f'The area is {r}'

def area_of_circle(r):

    c = r ** 2 * math.pi

    return f'The area is {c}'

# type_of_shape = ['triangle', 'rectangle','circle']

type_of_shape = input ('Chose a shape (triangle, rectangle, circle):')
print(type_of_shape)

if type_of_shape == 'triangle':

    base_of_triangle = input('Give base of the triangle:')
    print(base_of_triangle)

    height_of_triangle = input('Give height of the triangle: ')
    print(height_of_triangle)

    area = area_of_triangle(int(base_of_triangle), int(height_of_triangle))
    print(area)


elif type_of_shape == 'rectangle':

    base_of_rectangle = input('Give base of the rectangle:')
    print(base_of_rectangle)

    height_of_rectangle = input('Give height of the rectangle:')
    print(height_of_rectangle)

    area = area_of_rectangle(int(base_of_rectangle), int(height_of_rectangle))
    print(area)


elif type_of_shape == 'circle':

    radius_of_circle = input('Give radius of the circle:')
    print(radius_of_circle)

    area = area_of_circle(int(radius_of_circle))
    print(area)

else:
    print('Unknown shape!!')