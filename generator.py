import csv
import random

# Define the range for the random numbers
start = int(input("Enter Starting Range: "))
end = int(input("Enter Limit Range: "))
numOfDigits = int(input("Enter number of digits to be generated: "))
# Generate the random numbers
random_numbers = [[random.randint(start, end) for j in range(2)] for i in range(2500)]

# Write the numbers to a CSV file
with open("model.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(random_numbers)
