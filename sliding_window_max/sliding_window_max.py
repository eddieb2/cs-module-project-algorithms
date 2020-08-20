'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# Time Complexity O(n^2)
def sliding_window_max(nums, k):
    # list of maximum nums from each window shift
    max_list = []

    # loop through nums => len(nums) - k + 1 stops the window from moving past the end of the array
    for i in range(len(nums) - k + 1):
        # first for loop allows us to track the start and end of the window
        window_start = i
        window_end = i + k
        temp_list = []

        # second loop allows us to loop from start of the window and end of the window
        for j in range(window_start, window_end):
            # append all nums from the window to a new temp list
            temp_list.append(nums[j])

        # find the max number from the temp list and append to final array
        max_list.append(max(temp_list))

    return max_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
'''
Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


'''
