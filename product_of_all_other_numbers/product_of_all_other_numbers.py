'''
Input: a List of integers
Returns: a List of integers
'''
from math import prod

def product_of_all_other_numbers(arr):
    # create empty list
    prod_list = []
    # loop through arr
    # create a temp list to hold the nums that need multiplied
    # prod(temp_list)
    # then push it into prod list
    for i in range(len(arr)):
        temp_list = [arr[num] for num in range(len(arr)) if num != i]

        prod_list.append(prod(temp_list))

    return prod_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

'''

For example, given 
```
[1, 7, 3, 4]
```
your function should return 
```
[84, 12, 28, 21]
``` 
by calculating 
```
[7*3*4, 1*3*4, 1*7*4, 1*7*3]


'''