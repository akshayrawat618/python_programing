rows = int(input("Enter number of rows: "))

k = 0

#range function(0-no of rows)
for i in range(1, rows+1):
   
   # print(i)

    #first for  loop to print space 
    for space in range(1, (rows-i)+1):  #row value is given by user
        #ex(row value is 4 so (4-1))

        #print(space)
        print(end="  ")
   
   #second for lopp for print star4

    while k != (2*i-1):           #initially i=1

        #print(f"While loop Value of K:{k}") 
        print("* ", end="")
        k += 1
        #print(f"Value of K after increament:{k}")
        
   
    #k = 0
    print()