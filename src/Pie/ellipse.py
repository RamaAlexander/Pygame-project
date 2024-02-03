import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Drawing Ellipse")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    
    screen.fill((0, 0, 255))
    
    # draw a eclipse
    color = 255, 255,   0
    position = 240, 200, 640, 480
    width = 10
    pygame.draw.ellipse(screen, color, position, width)
    
    pygame.display.update()
    