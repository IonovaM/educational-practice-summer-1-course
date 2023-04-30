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

plt.show()