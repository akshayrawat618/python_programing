arr = [7,1,6,5,8]


'''
1. Sorting the array

'''

#Bubble Sort 
# Range() is define as start,stop and step So in our array start is the second last element in the array and 
#stop is the first element of the array and we need to move one step
def bubblesort(arr):
    for item in range(len(arr)-1,0,-1):
        print(f"Getting the Item {item}")
        for index in range(item):
            print(f"Getting the Index {index}")
            if arr[index] > arr[index+1]:
                temp = arr[index]
                arr[index] = arr[index +1]
                arr[index+1] = temp


bubblesort(arr)
print(arr)
