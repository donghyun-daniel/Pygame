import pygame
from Definition import *

class Screen():
    def __init__(self, bg, width, height): #self, background image, screen width, screen height
        self.screen = pygame.display.set_mode((width, height))
        self.bg=pygame.image.load(bg)
        self.screen.blit(self.bg, (0, 0))
        self.width=width
        self.height=height
    def draw_values(self, m, s, l, font_size): #self, money, score, life, font_size
        self.screen.blit(self.bg, (0, 0)) #Show Background
        mls_font= pygame.font.SysFont('georgia', font_size)
        money = mls_font.render('$ {}'.format(m), True, YELLOW)
        score = mls_font.render('Score : {}'.format(s), True, WHITE)
        life = mls_font.render('Life : {}'.format(l), True, RED)
        self.screen.blit(money, money.get_rect(centerx=self.width // 6, centery=50))
        self.screen.blit(score, score.get_rect(centerx=(self.width // 6) * 3, centery=50))
        self.screen.blit(life, life.get_rect(centerx=(self.width // 6) * 5, centery=50))