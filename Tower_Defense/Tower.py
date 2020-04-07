import pygame
from Definition import *
from Button import *

class Tower():  #ramnge, dmg, (atk_speed is lower is better)
    def __init__(self,pos_x, pos_y):
        self.level=0
        self.type=0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.button = pygame.Rect(0, 0, 50, 50)
        self.button.center = (self.pos_x, self.pos_y)
        self.price=0

    def upgrade(self, money):
        if money>=self.price*3 and self.level<3:
            money-=self.price*3
            self.level+=1
            self.dmg*=2
            self.atk_speed-=3
            if self.type==1:
                if self.level==1:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower1_1.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
                    self.range = 300
                    self.dmg = 40
                    self.atk_speed = 50
                    self.image = pygame.transform.scale(pygame.image.load("images/tower1_1.png").convert_alpha(),(50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
                elif self.level==2:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower1_2.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
                elif self.level==3:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower1_3.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
            elif type==2:
                if self.level==1:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower2_1.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
                    self.range = 100
                    self.dmg = 80
                    self.atk_speed = 30
                if self.level==2:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower2_2.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
                elif self.level==3:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower2_3.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
            elif type==3:
                if self.level==1:
                    self.image = pygame.transform.scale(pygame.image.load("images/tower3_1.png").convert_alpha(), (50, 50))
                    self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                    self.button.center = self.rect.center
                    self.range = 400
                    self.dmg = 70
                    self.atk_speed = 25
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

    def build_tower(self, type, money):  # pos is the value in the map_pos
        cost=0
        if type==1:
            cost=self.t1_price
        elif type==2:
            cost=self.t2_price
        elif type==3:
            cost=self.t3_price
        if money>=cost:



        txt_font = pygame.font.SysFont('georgia', 20)
        c = txt_font.render('CANCEL', False, RED)
        t1 = txt_font.render('$20', True, YELLOW)
        t2 = txt_font.render('$50', True, YELLOW)
        t3 = txt_font.render('$80', True, YELLOW)
        screen.blit(c, c.get_rect(centerx=l[0].button.centerx, centery=l[0].button.centery + 40))
        screen.blit(t1, t1.get_rect(centerx=l[1].button.centerx, centery=l[1].button.centery + 40))
        screen.blit(t2, t2.get_rect(centerx=l[2].button.centerx, centery=l[2].button.centery + 40))
        screen.blit(t3, t3.get_rect(centerx=l[3].button.centerx, centery=l[3].button.centery + 40))

        for i in l:
            b = Button.check_click(i, mouse, event, screen)
            if b != None:
                return b
        return False



    def sell(self, money):
        money+=(int(self.price*0.8))
        self.level = 0
        self.type = 0
        return money

tower_price=[[30,60,120],
             [50,100,200],
             [100,200,400]]

