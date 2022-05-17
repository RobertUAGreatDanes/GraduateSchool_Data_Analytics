# Robert Mornan
# 001336565
# INF 528
# Analysis, Visualization, and Prediction in Analytics


import matplotlib.pyplot as plt
import csv


y = []
x = []
# line plot
with open('pedalme_/pedalme_edges.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append((row[1]))

plt.plot(x, y, color='g', linestyle='dashed',
         marker='o', label="Delivery Data")

plt.xticks(rotation=25)
plt.xlabel('To')
plt.ylabel('Form')
plt.title('Pedal Me Edges', fontsize=20)
plt.grid()
plt.legend()
plt.show()