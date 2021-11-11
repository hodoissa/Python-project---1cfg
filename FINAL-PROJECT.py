
from gettext import install

import matplotlib
import pip
from matplotlib import pyplot as plt



#  first import csv
import csv

# 1) read csv file
with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))

#  2) Collect all of the sales from each month into a single list

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    sales = []

    for row in spreadsheet:
        sales_data = int(row['sales'])                    #  removes the string error from the values
        sales.append(sales_data)
    print(sales)

#  3) Output the total sales across all months

total = sum(sales)
print('Total sales across all months is: {}'.format(total))



# extension 1
# monthly changes as a percentage

import numpy as np
import pandas as pd
df = pd.read_csv ('sales.csv')
print(df)

sales_percentage = df['sales'].pct_change()   # sales monthly change
expenditure_percentage = df['expenditure'].pct_change()  # expenditure monthly change
print(sales_percentage)
print(expenditure_percentage)

# extension 2
# average sale

avg_sales = total / len(sales)
print(('Average sales across all months is: {}'.format(avg_sales)))

# extension 3
# Highest and lowest sales figures                           ## can be extended by finding the months

min_sales = min(sales)

max_sales = max(sales)

print('The highest number of sales made in a month was {}'.format(max_sales))
print('The lowest number of sales made in a month was {}'.format(min_sales))

# extension 4
# visualising data -- monthly sales


pip
install
matplotlib

import seaborn as seaborn

seaborn.set_theme()

seaborn.relplot(
    data=df,
    x='month' , y='sales')

seaborn.scatterplot(
    data=df,
    x='month', y='sales')

plt.title('Monthly Sales')
plt.show()