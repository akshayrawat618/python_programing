# This is the input value
arr = [2, 3, 4, 10, 40]
x = 10

def binarySearch(arr, l, r, x):
    '''
    This function is to run the biinary search and 
    get the value 
    l: left value in array
    r: right value in array
    x: target value
    Ex: []
    '''
    print("Checking if right value is greater then or equal to left value")
    if r >= l:
        print("Getting the mid value for the array")
        mid = l + (r - l) // 2

        if arr[mid] == x:
            print(f"Mid array: {arr[mid]} is Equal to Target value: {x} Got the value")
            return mid
        elif arr[mid] > x:
            print(f"Mid array: {arr[mid]} is greater then Target value: {x} Searching again")
            return binarySearch(arr, l, mid - 1, x)
        else:
            print(f"Mid array: {arr[mid]} is smaller then Target value: {x} Searching again")
            return binarySearch(arr,  mid + 1, r, x )
    else:
        print(f"Element: {x} is not present in the array:{arr}")
        return -1 


# Initating the  Binary search Function
result = binarySearch(arr, 0, len(arr)-1, x)