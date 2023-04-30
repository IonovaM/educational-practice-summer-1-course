# Создайте функцию, выводящую на изображение треугольник.
# Для всех точек вне треугольника оставьте только канал B.
# Все точки внутри треугольника переводятся в градации серого цвета.

# Задание 3, вариант 19, задача 6

import matplotlib.pyplot as plt
import skimage.io as io
import random

img = io.imread("/Users/margarita/PycharmProjects/учебная практика/ранго.jpeg")

def recolor(image):
    size_x = len(image[:])
    size_y = len(image[1])
    x5 = random.uniform(size_x/9, size_x)
    y5 = random.uniform(size_y/3, size_y/1.5)
    x6 = random.uniform(170, 400)
    y6 = random.uniform(100, 400)
    # координаты ромба
    x1 = x5 - x6
    x2 = x5
    x3 = x5 + x6
    x4 = x5
    y1 = y5
    y2 = y5 - y6
    y3 = y5
    y4 = y5 + y6

    for x in range(0, size_x):
        for y in range(0, size_y):
            a = (x1 - x) * (y2 - y) - (x2 - x) * (y1 - y)
            b = (x2 - x) * (y3 - y) - (x3 - x) * (y2 - y)
            c = (x3 - x) * (y4 - y) - (x4 - x) * (y3 - y)
            d = (x4 - x) * (y1 - y) - (x1 - x) * (y4 - y)

            if ((a >= 0 and b >= 0 and c >= 0 and d >= 0) or (a <= 0 and b <= 0 and c <= 0 and d >= 0)):
                image[x, y, 0:3] = [0, image[x, y, 1], 0]
            else:
                image[x, y, 0:3] = image[x, y, 0:3].dot([0.07, 0.72, 0.21])

recolor(img)
io.imshow(img)
plt.axis("off")
plt.show()
