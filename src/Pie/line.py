import sys
import random
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    
    screen.fill((0, 80, 0))
    pos_x1 = random.randint(0, 600)
    pos_y1 = random.randint(0, 500)
    pos_x2 = random.randint(0, 600)
    pos_y2 = random.randint(0, 500)
    
    # draw the line
    color = 100, 255, 200
    width = 8
    pygame.draw.line(screen, color, (pos_x1, pos_y1), (pos_x2, pos_y2), width)
    
    pygame.display.update()
    