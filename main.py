from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


print_matrix(matrix)
print("\n")
ident(matrix)
print("\n")
print_matrix(matrix)
print("\n")
#draw_lines( matrix, screen, color )
#display(screen)
add_point(matrix, 1, 2, 3)
print("\n")
print_matrix(matrix)
