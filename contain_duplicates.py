#Contain duplicates.
def get_duplicates(arr):
    sete = set(arr)
    print(sete)
    return len(arr) != len(set(arr))

arr = [1,3,0,2,3]
get_duplicates(arr)