#l1 = ["abs","def","xyz","lmn"]
ls = ["apa","rna","xkcd"]
#l1 = ["apa", "rna", "xkcd","lmn"]

'''
final_list = []
for items in l1:
    if 'items' not in final_list:
        final_list.append(items)

print(''.join(final_list))

final_list = []
for items in l1:
    for i in items:
        print(i)
        if i in final_list:
             final_list.remove(items)
        
print(final_list)
'''

for char in ls :
    counts=ls.count(char)
    while counts > 1:
        print(char,counts)

