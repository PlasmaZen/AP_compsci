# 17:19
import pygame as pg 
from math import *

pg.init()
WINDOW_SIZE = 800
screen = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pg.time.Clock()
running = True
dt = 0

projection_matrix = [[1,0,0],
                     [0,1,0],
                     [0,0,0]]

cube_points = [n for n in range(8)]
cube_points[0] = [[-1], [-1], [1]]
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

    product = [[0 for _ in range(b_cols)] for _ in range(a_rows)] #product matrix

    #this terrible nested for loop goes through each row/column and multiplies them
    if a_cols == b_rows: #checks if sizes are compatible
        for i in range(a_rows):
            for j in range(b_cols):
                for k in range(b_rows):
                    product[i][j] += a[i][k] * b[k][j]
    else:
        print("INCOMPATIBLE MATRIX SIZES")
    
    return product

scale = 100
angle_x = angle_y = angle_z = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    dt = clock.tick(60) / 1000 # sets frame rate to 60

    rotation_x = [[1, 0, 0],
                  [0, cos(angle_x), -sin(angle_x)],
                  [0, sin(angle_x), cos(angle_x)]]
    
    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                  [0, 1, 0],
                  [-sin(angle_y), 0, cos(angle_y)]]
    
    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                  [sin(angle_z), cos(angle_z), 0],
                  [0, 0, 1]]
    
    angle_x += 0.1

    for point in cube_points:
        rotate_x = multiply_m(rotation_x, point)
        rotate_y = multiply_m(rotation_y, rotation_x)
        rotate_z = multiply_m(rotation_z, rotation_y)
        point_2d = multiply_m(projection_matrix, point)

        x = (point_2d[0][0] * scale) + WINDOW_SIZE/2 # multiplying by scale because point origin is top left
        y = (point_2d[1][0] * scale) + WINDOW_SIZE/2

        pg.draw.circle(screen, (255, 0, 0), (x, y), 5)

    pg.display.flip() # updates screen

pg.quit()