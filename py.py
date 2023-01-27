from python_coding.matrix import Column


Row = int(input("Enter number of rows: ")) #Ask for your input, edit this as desired.
Column = int(input("Enter number of columns: "))

x = 4
#You want the range to start from 1

list_of_lists = [] 
#create a lists to store your columns

for row in range(Row):
    inner_list = []   
    #create the column
    
    for col in range(Column):
        inner_list.append(x)
         #add the x element and increase its value
      
        x=x+1
    list_of_lists.append(inner_list)
     #add it

for internalList in list_of_lists: #this is just formatting.
    print(str(internalList)+"\n")