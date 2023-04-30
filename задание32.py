# Создайте функцию, выводящую на изображение ромб.
# Все точки вне ромба переводятся в градации серого цвета.
# Для всех точек внутри ромба оставьте только канал G.

# Задание 3, вариант 19, задача 7

import matplotlib.pyplot as plt
import skimage.io as io
import random

img = io.imread("/Users/margarita/PycharmProjects/учебная практика/зверополис3.jpeg")

def recolor(image):
    # координаты треугольника
    x1 = random.uniform(0, len(image[:]))
    x2 = random.uniform(0, len(image[:]))
    x3 = random.uniform(0, len(image[:]))
    y1 = random.uniform(0, len(image[1]))
    y2 = random.uniform(0, len(image[1]))
    y3 = random.uniform(0, len(image[1]))
    size_x = len(image[:])
    size_y = len(image[1])
    for x in range(0, size_x):
        for y in range(0, size_y):
            a = (x1 - x) * (y2 - y) - (x2 - x) * (y1 - y)
            b = (x2 - x) * (y3 - y) - (x3 - x) * (y2 - y)
            c = (x3 - x) * (y1 - y) - (x1 - x) * (y3 - y)

            if ((a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0)):
                image[x, y, 0:3] = image[x, y, 0:3].dot([0.07, 0.72, 0.21])
            else:
                image[x, y, 0:3] = [0, 0, image[x, y, 2]]

recolor(img)
io.imshow(img)
plt.axis("off")
plt.show()
