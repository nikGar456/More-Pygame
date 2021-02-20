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

"""Canvas or a screen"""
width, height = 500, 500
screen = pg.display.set_mode([width, height])
pg.display.set_caption("hello")

# pg.display.flip()
pg.display.update()

gameExit = False

while not gameExit:
    for event in pg.event.get():
        print(event)
        """Lets add an event handler for quiting the window"""
        if event.type == pg.QUIT:
            gameExit = True

        screen.fill(white)
        """Draw a rectangle here"""
        pg.draw.rect(screen, red, (150, 150, 50, 25))
        pg.draw.rect(screen, black, (250, 250, 100, 50))
        pg.display.update()

pg.quit()
quit()
