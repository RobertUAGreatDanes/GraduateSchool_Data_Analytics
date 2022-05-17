# Robert Mornan
# 001336565
# INF 528
# Analysis, Visualization, and Prediction in Analytics


import matplotlib.pyplot as plt
import pandas as pd
import csv


df = pd.read_csv('name_gender_dataset.csv')
names_data = df['Name']
prob_data = df['Probability']
plt.pie(prob_data, labels=names_data, shadow=True, startangle=140)
plt.title('Probability of Names')
plt.show()
