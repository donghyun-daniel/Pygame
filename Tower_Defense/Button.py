import pygame
from Definition import *

class Button():
    def __init__(self, pos_x, pos_y, w, h):
        self.width, self.height = w, h
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.button=pygame.Rect(0,0,self.width,self.height)
        self.button.center=(self.pos_x,self.pos_y)
        self.font=False
    def draw(self, s):
        pygame.draw.rect(s,GREY, self.button)
        if self.font:
            s.blit(self.font,self.font.get_rect(centerx=self.pos_x, centery=self.pos_y))
    def check_click(self,mouse_pos, event,screen):
        if self.button.collidepoint(mouse_pos):
            if self.font:
                self.font = pygame.font.SysFont('georgia', self.font_size).render(self.txt, True, BLUE)
                screen.blit(self.font, self.font.get_rect(centerx=self.pos_x, centery=self.pos_y))
            for e in event:
                if e.type==pygame.MOUSEBUTTONDOWN:
                    return self
                else:
                    return False
        else:
            if self.font:
                self.font = pygame.font.SysFont('georgia', self.font_size).render(self.txt, True, RED)
                screen.blit(self.font, self.font.get_rect(centerx=self.pos_x, centery=self.pos_y))
    def add_txt(self, font_size, txt):
        self.txt = txt
        self.font_size = font_size
        self.font = pygame.font.SysFont('georgia', self.font_size).render(txt, True, RED)