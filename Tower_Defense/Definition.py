import pygame

#init some config

#Color Definition
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (50,50,50)

S_WIDTH, S_HEIGHT = 1200, 800

pygame.init()
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)
pygame.display.set_caption("Tower Defense v1")