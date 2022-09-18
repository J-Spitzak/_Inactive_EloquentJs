# List operations
### easy

Suppose a list called coefficients currently contains the following values:
{1, 3, 5, 2, 4}.
What is displayed after the following code segment is executed?
REMOVE(coefficients, 2)
APPEND(coefficients, 5)
INSERT(coefficients, 3, 11)
DISPLAY(coefficients[1] + coefficients[2] + LENGTH(coefficients))

## Explanation
the question performs operations on a list of numbers then takes some values 
from it and adds them together then prints them

## solution
there are 3 factors that are added together
1. the length of the list
    - the list starts at 5 items
    - a item is removed, appended and inserted
    - the net result is +1 value
    - the final length is 6
2. coefficients[1]
    - everything that is changed in the list happens after 1
    - this values remains 1
3. coefficients[2]
    - only REMOVE(coefficients, 2) changes the value of coefficients[2]
    - coefficients[2] becomes 5
4. add em' all up
    - 6(length) + 1(coefficients[1]) + 5(coefficients[2])
### solution is 12



