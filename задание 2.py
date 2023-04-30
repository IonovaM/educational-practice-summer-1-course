import math
import linecache
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import matplotlib.ticker as ticker

fig = plt.figure()
fig.set_size_inches(16, 12)
ax_1 = fig.add_subplot(231)
ax_2 = fig.add_subplot(232)

with cbook.get_sample_data('/Users/margarita/PycharmProjects/учебная практика/2022-07-25 19.28.33.jpg') \
        as image_file:
            image = plt.imread(image_file)
            ax_1.imshow(image)
            ax_1.text(250, 150, u"Белое здание",  fontsize = 15, fontfamily = 'Arial', color = '#082567', style = 'italic', fontweight='bold')
            ax_1.set_xticks([])
            ax_1.set_yticks([])

# задание 1.2
data = []
count = 0
with open("/Users/margarita/PycharmProjects/учебная практика/file_date.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])
        if count == 0:
            x = np.array([float(r) for r in line.split()])
        if count == 19:
            y = np.array([float(t) for t in line.split()])
        count += 1
ax_2.fill_between(x, y, 0, where = (y <= 0), alpha = 0.44,  color = 'blueviolet')
ax_2.fill_between(x, y, 0, where = (y >= 0), alpha = 0.8, color = 'deeppink')
#plt.grid(True)
# подпись осей
ax_2.set_xlabel('Время', fontsize = 15, fontfamily = 'Arial', color = '#551A8B', style = 'italic', fontweight='bold')
ax_2.set_ylabel('Температура', fontsize = 15, fontfamily = 'Arial', color = '#8B2252', style = 'italic', fontweight='bold')
# организация разметки графика
ax_2.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax_2.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax_2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax_2.yaxis.set_minor_locator(ticker.MultipleLocator(22))
# стиль основных линий
ax_2.grid(which='major', color = 'k')
# видимость дополнительных делений
ax_2.minorticks_on()
# стиль дополнительных линий
ax_2.grid(which='minor', color = 'gray', linestyle = ':')
# подпись делений
ax_2.tick_params(labelrotation = 30, pad = 1, labelsize = 14, direction = 'out')

ax_3 = fig.add_subplot(233)
ax_4 = fig.add_subplot(234)
ax_5 = fig.add_subplot(235)
ax_6 = fig.add_subplot(236)




# задание 2.1
#  получаю начальное и конечное значения интервала для оси абсцисс диаграммы
with open("/Users/margarita/PycharmProjects/учебная практика/fig8.txt", "r") as f: text = f.readlines()
a, b = map(int, text[36].split())

# список всех значений по оси x
xvalue = []
for i in range(a, b + 1):
    xvalue.append(i)

# список значений по оси y
yvalue = []
for i in linecache.getline("/Users/margarita/PycharmProjects/учебная практика/fig8.txt", 38).split():
    yvalue.append(int(i))

# создание аннотации и стрелки
arrowprops = dict(arrowstyle = '->', color = (0.545, 0.243, 0.184), connectionstyle = 'arc3,rad=-0.5')
plt.annotate(u'Максимум', fontfamily = "Arial", color = '#CD5B45', fontsize = 13, fontstyle='normal',
             fontweight='normal', xy=(293, 15.9), xytext = (279, 14), arrowprops = arrowprops)

ax_3.set_facecolor("#FAF0E6")
ax_3.bar(xvalue, yvalue, color = "#FFA07A")







# задание 2.2
y1 = []
y2 = []
x = np.arange(-3, 3, 0.05)
poly = np.poly((-1.63, -0.44, 0.35, 1.9))
for i in x:
    y1.append((math.sin(2 * i)) ** 2 - (math.cos(6 * i)) ** 2)
    y2.append(0.3 * np.polyval(poly, i))

# создание графиков
ax_4.plot(x, y1, linestyle='dashed', color = '#ff033e', label='График по y1')
ax_4.plot(x, y2, linestyle='dashdot', color = '#03ceff', label='График по y2')
# настройка легенды
font = font_manager.FontProperties(family='Tahoma', weight='bold', style='italic', size=13)
ax_4.legend(loc='best', prop=font, labelcolor = '#003153')
# поворот подписей делений оси
ax_4.tick_params(axis = 'x', labelrotation=45)







# задание 2.3
x1 = np.random.rand(300)
x2 = np.random.rand(300) + 1
x3 = np.random.rand(300) + 2

y1 = np.random.normal(7, 3, 300)            #нормальное распределение
y2 = np.random.uniform(0, 10, 300)          #равномерное распределение
y3 = np.random.gamma(0.8, 1.7, 300)         #гамма распределение

ax_5.scatter(x1, y1, s=2, color=(1, 1, 0.25))
ax_5.scatter(x2, y2, s=2, color='#60FF60')
ax_5.scatter(x3, y3, s=2, color='w')
# цвет фона
ax_5.set_facecolor('k')






# задание 2.4
t = np.arange(0, 8 * math.pi, 0.0001)
x = []
y = []
for i in t:
    x.append(3 * math.sin(4.5 * i + math.pi/8))
    y.append(8.5 * math.sin(11.5 * i))

ax_6.fill_between(x,y, alpha = 0.6, color = 'blueviolet')
ax_6.grid(color = 'blue')



plt.show()
fig.savefig('saved_figure.png')


