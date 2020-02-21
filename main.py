from display import *
from draw import *
from matrix import *
import random

#Testing functions
print("\nMaking new matrix. m1 = ")
m1 = new_matrix()
print_matrix(m1)

print("\nTesting ident(). m1 = ")
ident(m1)
print_matrix(m1)

print("\nMaking new matrix. m2 = ")
m2 = [[1,2,3,1],[4,5,6,1],[7,8,9,1],[1,1,1,1]]
print_matrix(m2)

print("\nTesting matrix_mult(). m1 * m2 = ")
matrix_mult(m1, m2)
print_matrix(m2)

print("\nTesting add_point() to new matrix. Adding (0,0,0), (1,2,3). m3 = ")
m3 = []
add_point(m3, 0, 0, 0)
add_point(m3, 1, 2, 3)
print_matrix(m3)

print("\nTesting add_edge(). Adding (4,5,6), (7,8,9). m3 = ")
add_edge(m3, 4, 5, 6, 7, 8, 9)
print_matrix(m3)

print("\nTesting matrix_mult(). m2 * m3 = ")
matrix_mult(m2, m3)
print_matrix(m3)

#Making drawing
screen = new_screen()
matrix = []
matrix1 = []
for a in range(250):
    add_edge(matrix, random.randrange(500), random.randrange(500), random.randrange(500), random.randrange(500), random.randrange(500), random.randrange(500))
    add_edge(matrix1, random.randrange(500), random.randrange(500), random.randrange(500), random.randrange(500), random.randrange(500), random.randrange(500))
draw_lines(matrix, screen, [random.randrange(255),random.randrange(255),random.randrange(255)])
draw_lines(matrix1, screen, [random.randrange(255),random.randrange(255),random.randrange(255)])

display(screen)
save_ppm(screen, 'binary.ppm')
save_ppm_ascii(screen, 'ascii.ppm')
save_extension(screen, 'img.png')
