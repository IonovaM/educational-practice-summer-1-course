# Разработайте функцию, которая переводит каждый нечетный
# столбец пикселей (вертикальные линии) в градации серого цвета.
# Задание 3, вариант 19, задача 9

# Разработайте функцию, которая переводит каждый нечетный
# столбец пикселей (вертикальные линии) в градации серого цвета.
# Задание 3, вариант 19, задача 19

import matplotlib.pyplot as plt
import skimage.io as io

img = io.imread("/Users/margarita/PycharmProjects/учебная практика/джери2.jpeg")

def recolor(image):
    size_x = len(image[:])
    size_y = len(image[1])
    for x in range(0, size_x):
        for y in range(0, size_y):
            if (y % 2 != 0):
                image[x, y, 0:3] = image[x, y, 0:3].dot([0.07, 0.72, 0.21])

recolor(img)
io.imshow(img)
plt.axis("off")
plt.show()
