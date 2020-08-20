'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # sort -> reverse
    arr.sort()

    # moves all negatives to the end of list
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr.append(arr[i])
            arr.pop(i)

    # puts all non-zeros at front and zeros at the end
    arr.reverse()

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")