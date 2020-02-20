from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

for col in range(len(matrix)):
    for row in range(len(matrix[col])):
        if(row == 3):
            matrix[col][row] = 1
        else:
            matrix[col][row] = random.randrange(500)

matrix1 = [[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]]

ident(matrix)
matrix[0][0] = 3

print_matrix(matrix)
print("\n")
print_matrix(matrix1)
print("\n")
matrix_mult(matrix, matrix1)
print_matrix(matrix1)
