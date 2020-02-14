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

matrix1 = [[100, 4, 0, 1],[32, 495, 0, 1],[433, 54, 0, 1],[133, 14, 0, 1],[9, 214, 0, 1],[13, 20, 0, 1],[353, 484, 0, 1],[123, 64, 0, 1],[1, 304, 0, 1]]


print_matrix(matrix)
print("\n")
print_matrix(matrix1)
print("\n")
matrix_mult(matrix, matrix1)
