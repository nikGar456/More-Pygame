"""
PyGAME: It is like Turtle but much bigger.
https://www.pygame.org/
"""

import pygame as pg
import time

pg.init()

""" () is a tuple """
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

"""Here we define variables"""
width, height = 500, 500
block_size = 10

"""Canvas or a screen"""
screen = pg.display.set_mode([width, height])
pg.display.set_caption("hello")

# pg.display.flip()
pg.display.update()

gameExit = False
snake_x = width/2
snake_y = height/2
snake_x_change = 0
snake_y_change = 0

# FPS - Frames Per Seconds
fps = 15
clock = pg.time.Clock()

while not gameExit:
    for event in pg.event.get():
        # print(event)
        """Lets add an event handler for quiting the window"""
        if event.type == pg.QUIT:
            gameExit = True
        """ This is listening to KEYDOWN event"""
        if event.type == pg.KEYDOWN:
            # print("key pressed")
            if event.key == pg.K_LEFT:
                snake_x_change = -10
                snake_y_change = 0
            if event.key == pg.K_RIGHT:
                snake_x_change = 10
                snake_y_change = 0
            if event.key == pg.K_UP:
                snake_y_change = -10
                snake_x_change = 0
            if event.key == pg.K_DOWN:
                snake_y_change = 10
                snake_x_change = 0


    snake_x += snake_x_change
    snake_y += snake_y_change
    print(snake_x, snake_y)

    """Add the code to detect the walls"""
    if snake_x > width or snake_x < 0 or snake_y > height or snake_y < 0:
        gameExit = True


    screen.fill(white)
    """Draw a rectangle here"""
    # pg.draw.rect(screen, red, (150, 150, 50, 25))
    pg.draw.rect(screen, black, (snake_x, snake_y, block_size, block_size))
    pg.display.update()
    clock.tick(fps)


font = pg.font.Font(None, 34)
text = font.render("Game Over", True, red, black)
screen.blit(text, (200, 200))
pg.display.update()

time.sleep(2)

pg.quit()
quit()
