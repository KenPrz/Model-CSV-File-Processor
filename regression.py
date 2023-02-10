import numpy as np
import csv
import datetime
# Reading data from the CSV file
file_name1 = str(input("Enter the name of the csv file: "))
x, y = [], []
with open(file_name1, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        x.append([float(row[0])])
        y.append([float(row[1])])
# Computing the mean of the data
xBar = np.mean(x)
yBar = np.mean(y)
# x - x̄
xSubracted_To_xBar = np.subtract(x,xBar)
ySubracted_To_yBar = np.subtract(y,yBar)

product_Of_xSubracted_To_xBar_And_ySubracted_To_yBar = np.multiply(xSubracted_To_xBar,ySubracted_To_yBar)
xSubracted_To_xBar_Squared = np.power(xSubracted_To_xBar,2)
# getting summation
summationOne = np.sum(product_Of_xSubracted_To_xBar_And_ySubracted_To_yBar)
summationTwo = np.sum(xSubracted_To_xBar_Squared)
# slope
slope = summationOne/summationTwo
yIntercept = yBar - slope * xBar
print('xBar: '+str(xBar))
print('yBar: '+str(yBar))
print('Slope: '+str(slope))
print('y-Intercept: '+str(yIntercept))

#read file2
file_name = str(input("Enter the name of the csv file: "))
x_indipendent,y_dependent = [],[]
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        x_indipendent.append([float(row[0])])

#y = mx + b = 0.964 x 12 + 0.434
y_dependent = np.multiply(slope, np.array(x_indipendent)) + yIntercept

#writing to file
today = str(datetime.datetime.now().date())
new_file_name = file_name.split('.csv')[0] + '_Processed_Data_ON_' + today + '.csv'
with open(new_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    for x, y in zip(x_indipendent, y_dependent):
        writer.writerow([x[0], y[0]])