# Robert Mornan
# 001336565
# INF 528
# Analysis, Visualization, and Prediction in Analytics


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# import data using pandas
df = pd.read_csv('name_gender_dataset.csv')

# data to be plotted
data = df['Probability']
bs = np.arange(min(data), max(data) + 1, 5)

x = df.loc[df['Name'] == 'name']
y = df.loc[df['Gender'] == 'gender']

plt.hist(y['Gender'], bs, label='names', color='maroon')

plt.legend()
plt.show()