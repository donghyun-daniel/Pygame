import pygame
import time
import random
import math

#Color Definition
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (100,100,100)

S_WIDTH, S_HEIGHT = 1200, 800

#init
pygame.init() #파이 게임 초기화
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)
pygame.display.set_caption("Tower Defense v1")
bg=pygame.image.load("images/background.png")

class Screen():
    def __init__(self, bg, width, height, objects):
        self.screen = pygame.display.set_mode((width, height))
        self.bg=pygame.image.load(bg)
        self.screen.blit(self.bg, (0, 0))
        self.width=width
        self.height=height
    def draw(self,objects):
        for obj in objects:
            obj.draw(obj, self.screen)





class Button():
    def __init__(self, pos_x, pos_y, font_size, txt):
        self.width, self.height = len(txt)*int(font_size*0.8), int(font_size*1.2)
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.font_size=font_size
        self.txt=txt
        self.font=pygame.font.SysFont('georgia', self.font_size).render(self.txt,True,WHITE)
        self.button=pygame.Rect(0,0,self.width,self.height)
        self.button.center=(self.pos_x,self.pos_y)
    def draw(self,screen):
        pygame.draw.rect(screen,BLACK, self.button)
        screen.blit(self.font,self.font.get_rect(centerx=self.pos_x, centery=self.pos_y))
    def check_click(self,mouse_pos, event,screen):
        if self.button.collidepoint(mouse_pos):
            self.font = pygame.font.SysFont('georgia', self.font_size).render(self.txt, True, BLUE)
            first_screen.screen.blit(self.font, self.font.get_rect(centerx=self.pos_x, centery=self.pos_y))
            for e in event:
                if e.type==pygame.MOUSEBUTTONDOWN:
                    return True
                else:
                    return False
objects=[]
start=Button(S_WIDTH//2, int(S_HEIGHT//2 * (3/4)), 80, "START")
objects.append(start)
first_screen = Screen("images/background.png", 1200, 800, objects)
while True:
    Screen.draw(first_screen, objects)
    event=pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            pygame.quit()
    if Button.check_click(start, pygame.mouse.get_pos(), event, first_screen):
        print(1)
    pygame.display.flip()
pygame.quit()
