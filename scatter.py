# Robert Mornan
# 001336565
# INF 528
# Analysis, Visualization, and Prediction in Analytics

import matplotlib.pyplot as plt
import csv


# scatterplot
x = []
y = []

with open('name_gender_dataset.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append((row[3]))


plt.scatter(x, y, color='g', s=100)
plt.xticks(rotation=25)
plt.xlabel('Names')
plt.ylabel('Probabiltiy')
plt.title('Probability of A Person Name', fontsize=20)
plt.show()
