import pygame
from Definition import *

class Tower():
    def __init__(self, type, pos_x, pos_y):
        self.type=type
        self.level=1
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.button = pygame.Rect(0, 0, self.width, self.height)
        self.button.center = (self.pos_x, self.pos_y)
        #ramnge, dmg, atk_speed is lower is better
        if self.type==1:
            self.range=300
            self.dmg=40
            self.atk_speed=50
            self.price=30
            self.image = pygame.transform.scale(pygame.image.load("images/tower1_1.png").convert_alpha(), (50, 50))
            self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
            self.button.center = self.rect.center
        elif self.type==2:
            self.range=100
            self.dmg=80
            self.atk_speed=30
            self.price=40
            self.image = pygame.transform.scale(pygame.image.load("images/tower2_1.png").convert_alpha(), (50, 50))
            self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
            self.button.center = self.rect.center
        elif self.type==3:
            self.range=400
            self.dmg=70
            self.atk_speed=25
            self.price=100
            self.image = pygame.transform.scale(pygame.image.load("images/tower3_1.png").convert_alpha(), (50, 50))
            self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
            self.button.center = self.rect.center

    def upgrade(self, money):
        if money>=self.price*2 and self.level<3:
            money-=self.price*2
            self.level+=1
            self.dmg*=2
            self.atk_speed-=3
            if type==1:
                if self.level==2:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower1_2.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
                elif self.level==3:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower1_3.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
            elif type==2:
                if self.level==2:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower2_2.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
                elif self.level==3:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower2_3.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
            elif type==3:
                if self.level==2:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower3_2.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
                elif self.level==3:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower3_3.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
            return money
        else:
            return 0

        def check_click(self, mouse_pos, event, screen):
            if self.button.collidepoint(mouse_pos):
                for e in event:
                    if e.type == pygame.MOUSEBUTTONDOWN: #When click the Tower
                        pass



    def sell(self, money):
        money+=(int(self.price*0.8))
        del self
        return money


