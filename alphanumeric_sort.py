
lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']

def sort(lst):
    lst = [str(i) for i in lst]
    lst.sort()

#print(sort(lst))

def sort_key(lst):
    lst.sort(key = str)
    return lst

print(sort_key(lst))