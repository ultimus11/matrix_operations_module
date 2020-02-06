import matrices_operations as mo

# these are matrices to be added or multiplied. two matrices x and y should be given by user

x = [[1,7,3,4],
    [4 ,5,6,4],
    [7 ,8,9,4]]

y  = [[5,8,1,0],
    [6,7,3,0],
    [4,5,9,0]]

# following code is for addition of matrices
#usage: mo.add(matrix1,matrix2)
for r in mo.add(x,y):
 print(r)


# following code is for multiplicaztion of the matrices
#usage: mo.multiply(matrix1,matrix2)
for r in mo.multiply(x,y):
  print(r)


#following code is for transpose of the matrix
#usage: mo.transpose(matrix1)
for r in mo.transpose(x):
  print(r)