import pygame as pg
from math import *
import numpy as np

WINDOW_SIZE = 200
ROTATE_SPEED = 0.01
window = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pg.time.Clock()
pg.display.set_caption('')

projection_matrix = [[0.5, 0, 0],
                     [0, 0.5, 0], # affects L.W.H of rectangle
                     [0 , 0, 0]]

# these are the points that make up the cube
cube_points = [n for n in range(8)] # iterates through cube points
cube_points[0] = [[-1], [-1], [1]] # position of points in respect to center
cube_points[1] = [[1], [-1], [1]]
cube_points[2] = [[1], [1], [1]]
cube_points[3] = [[-1], [1], [1]]
cube_points[4] = [[-1], [-1], [-1]]
cube_points[5] = [[1], [-1], [-1]]
cube_points[6] = [[1], [1], [-1]]
cube_points[7] = [[-1], [1], [-1]]

def connect_points(i, j, points):
    pg.draw.line(window, (255, 255, 255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))

scale = 100
angle_x = angle_y = angle_z = 0
point_x = point_y = 0
while True:
    clock.tick(120)
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
    
    translation_x = [[1, 0, point_x],
                    [0, 1, 0],
                    [0, 0, 1]]

    translation_y = [[1, 0, 0],
                    [0, 1, point_y],
                    [0, 0, 1]]

    
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
           angle_x += 0.01
    if keys[pg.K_s]:
            angle_x -= 0.01
    if keys[pg.K_d]:
           point_x += 1
    if keys[pg.K_a]:
            point_x -= 1      

   # mouse_pos = pg.mouse.get_rel(i, j)
   # if mouse_pos[]
   # )
    points = [0 for _ in range(len(cube_points))]
    i = 0

    for point in cube_points:
        rotate_x = np.matmul(rotation_x, point)
        rotate_y = np.matmul(rotation_y, rotate_x)
        rotate_z = np.matmul(rotation_z, rotate_y)
        point_2d = np.matmul(projection_matrix, rotate_z)
        translation_x = np.add(projection_matrix, translation_x)
        translation_y = np.add(projection_matrix, translation_y)
    
        x = (point_2d[0][0] * scale) + WINDOW_SIZE/2 # centers points because they draw from top left
        y = (point_2d[1][0] * scale) + WINDOW_SIZE/2

        points[i] = (x,y) # what is happening here
        i += 1
        pg.draw.circle(window, (255, 255, 255), (x, y), 2.5)

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

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        
    pg.display.update()
