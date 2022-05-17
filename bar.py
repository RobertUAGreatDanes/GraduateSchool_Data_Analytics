# Robert Mornan
# 001336565
# INF 528
# Analysis, Visualization, and Prediction in Analytics

import matplotlib.pyplot as plt
import csv

y = []
x = []

# bar graph

x = []
y = []

with open('name_gender_dataset.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[1])
        y.append((row[2]))

plt.bar(x, y, color = 'g', width = 0.72, label = "probability")
plt.xlabel('Names')
plt.ylabel('Probability')
plt.title('Ages of different persons')
plt.legend()
plt.show()
