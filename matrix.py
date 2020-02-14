"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for row in range(4):
        rowMake = ""
        for col in range(len(matrix)):
            rowMake += str(matrix[col][row])
            if(matrix[col][row] < 10):
                rowMake += "   "
            elif(matrix[col][row] < 100):
                rowMake += "  "
            else:
                rowMake += " "
        print(rowMake)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            if(row == 3 or col == row):
                matrix[col][row] = 1
            else:
                matrix[col][row] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #pass
    for i in range(4): #rows in m1
        for col in m1: #cols in m2
            print(col[i])
            





def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
