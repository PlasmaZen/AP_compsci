# needs lines drawn between points
import pygame
from math import *

WINDOW_SIZE = 200
ROTATE_SPEED = 0.01
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()

projection_matrix = [[0.5,0,0],
                     [0,0.5,0], # affects L.W.H of rectangle
                     [0,0,0]]

cube_points = [n for n in range(8)] # iterates through cube points
cube_points[0] = [[-1], [-1], [1]] # position of points in respect to center
cube_points[1] = [[1], [-1], [1]]
cube_points[2] = [[1], [1], [1]]
cube_points[3] = [[-1], [1], [1]]
cube_points[4] = [[-1], [-1], [-1]]
cube_points[5] = [[1], [-1], [-1]]
cube_points[6] = [[1], [1], [-1]]
cube_points[7] = [[-1], [1], [-1]]

# THIS FUNCTION IS VERY INEFFICIENT
# learn how to use numpy to set up matrices and multiply
def multiply_m(a, b):
    a_rows = len(a) # takes the list
    a_cols = len(a[0]) # indexes the list like a column

    b_rows = len(b)
    b_cols = len(b[0])

    product = [[0 for i in range(b_cols)] for i in range(a_rows)] #product matrix

    #this terrible nested for loop goes through each row/column and multiplies them
    if a_cols == b_rows: #checks if sizes are compatible
        for i in range(a_rows):
            for j in range(b_cols):
                for k in range(b_rows):
                    product[i][j] += a[i][k] * b[k][j]
    else:
        print("INCOMPATIBLE MATRIX SIZES")
    
    return product

def connect_points(i, j, points):
    pygame.draw.line(window, (255, 255, 255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))
 #something wrong here 20:29
scale = 100
angle_x = angle_y = angle_z = 0
while True:
    clock.tick(60)
    window.fill((0,0,0))
    rotation_x = [[1, 0, 0],
                    [0, cos(angle_x), -sin(angle_x)],
                    [0, sin(angle_x), cos(angle_x)]]

    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                    [0, 1, 0],
                    [-sin(angle_y), 0, cos(angle_y)]]

    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                    [sin(angle_z), cos(angle_z), 0],
                    [0, 0, 1]]

    angle_x += 0.005
    angle_y += 0.005
    angle_z += 0.005

    points = [0 for _ in range(len(cube_points))]
    i = 0
    for point in cube_points:
        rotate_x = multiply_m(rotation_x, point)
        rotate_y = multiply_m(rotation_y, rotate_x)
        rotate_z = multiply_m(rotation_z, rotate_y)
        point_2d = multiply_m(projection_matrix, rotate_z)
    
        x = (point_2d[0][0] * scale) + WINDOW_SIZE/2 # centers points because they draw from top left
        y = (point_2d[1][0] * scale) + WINDOW_SIZE/2

        points[i] = (x,y)
        i += 1
        pygame.draw.circle(window, (255, 255, 255), (x, y), 2.5)

    connect_points(0, 1, points)
    connect_points(0, 3, points)
    connect_points(0, 4, points)
    connect_points(1, 2, points)
    connect_points(1, 5, points)
    connect_points(2, 3, points)
    connect_points(2, 6, points)
    connect_points(3, 7, points)
    connect_points(4, 7, points)
    connect_points(4, 5, points)
    connect_points(6, 5, points)
    connect_points(6, 7, points)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()