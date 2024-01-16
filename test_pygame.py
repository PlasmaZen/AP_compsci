import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 400))
clock = pg.time.Clock()
running = True
dt = 0

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("black")

    pg.draw.circle(screen, "red", player_pos, 10)
    pg.draw.line(screen, "white", (50, 50), (screen.get_width() - 50, 50))

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player_pos.y -= 300 * dt
    if keys[pg.K_s]:
        player_pos.y += 300 * dt
    if keys[pg.K_a]:
        player_pos.x -= 300 * dt
    if keys[pg.K_d]:
        player_pos.x += 300 * dt

    pg.display.flip()

    dt = clock.tick(60) / 1000

pg.quit()