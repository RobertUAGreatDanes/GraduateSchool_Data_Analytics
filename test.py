
# setup the figure size
plt.rcParams['figure.figsize'] = (8, 8)

# import csv file
data = 'name_gender_dataset.csv'

# import data using pandas
df = pd.read_csv('name_gender_dataset.csv')

# print the first 8 rows of the csv file
print(df.head(8))

# Display the box plot based on parameter used
plt.boxplot(data)

# show boxplot
plt.show()

x = []
y = []
# line plot
with open('name_gender_dataset.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(float(row[3]))

plt.pie(y, labels=x, autopct='%.2f%')
plt.title('Names of a Person')
plt.show()




# histogram



