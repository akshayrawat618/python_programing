#Merged to sorted list 

def merge_array(list1, list2):
    ind1 = 0 
    ind2 = 0
    while ind1 < len(list1) and ind2 < len(list2):
        if(list1[ind1] > list2[ind2]):
            list1.insert(ind1, list2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1
    
    if ind2 < len(list2):
        list1.extend(list2[ind2:])
    return list1

print(merge_array([4,5,6], [-2,-1,0]))