# Model-CSV-File-Processor

This code processes a CSV file containing data in the format of two columns, where the first column represents the independent variable (x) and the second column represents the dependent variable (y). The code then computes the slope and y-intercept of the data and generates a new processed data file.

## Dependencies
+ `numpy`
+ `csv`
+ `datetime`

## Input
```
x,y
value1,value2
...
value_n,value_n+1

```
The code will prompt the user to input the name of the CSV file.

## The code outputs the slope (m) and y-intercept (b) of the data and generates a new processed data file containing the calculated values of the dependent variable (y). The file is saved in the following format:

```
x,y
value1,mx + b
...
value_n,mx + b

```

## How it works

+ The code reads the data from the CSV file and stores the values of x and y in separate arrays.
+ The mean of the x and y arrays is computed using the numpy function mean.
+ The x and y arrays are subtracted by their respective mean to get x - x̄ and y - ȳ.
+ The product of x - x̄ and y - ȳ is computed and stored in a separate array.
+ The square of x - x̄ is computed and stored in a separate array.
+ The sum of the arrays obtained in step 4 and 5 are computed and stored in two separate variables.
+ The slope (m) is computed as the ratio of the sum of the product array to the sum of the square array.
+ The y-intercept (b) is computed as yBar - m * xBar.
+ The code prompts the user to input the name of the new data file.
+ The values of the dependent variable (y) are computed using the formula y = mx + b.
+ The new processed data file is saved in the format ``<input_file_name>_Processed_Data_ON_<today's_date>.csv.```

## Conclusion
This code provides a convenient way to process a CSV file containing data in a specified format and generate a new processed data file. The calculated values of the slope and y-intercept can be useful in making predictions based on the data.
