
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of column:"))
  
# Initialize matrix
matrix = []

  
'''
#For taking input from user
#A for loop for row entries
'''
for i in range(Row):          
    a =[]
    for j in range(Column):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
  
# For printing the matrix
for i in range(Row):
    for j in range(Column):
        print(matrix[i][j], end = " ")
    print()

