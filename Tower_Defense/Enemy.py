import pygame
from Definition import *

class Enemy():
    def __init__(self, hp, gold, kind):
        if kind=="small":
            self.image = pygame.transform.scale(pygame.image.load("images/enemy_small.png").convert_alpha(), (50, 50))
            self.speed = 3
        elif kind=="big":
            self.image = pygame.transform.scale(pygame.image.load("images/enemy_big.png").convert_alpha(), (50, 50))
            self.speed = 2
        self.hp=hp
        self.gold=gold
        self.button = pygame.Rect(100, 100, 50, 50)
        self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
        self.button.center = self.rect.center
        self.index=0

    def draw_Enemy(self, s):
        s.blit(self.image, self.button.topleft)

    def move_Enemy(self, r):
        if self.index==len(r):
            return self
        elif self.button.centerx!=r[self.index][0] or self.button.centery!=r[self.index][1]:
            if self.button.centerx<r[self.index][0]:
                self.button.centerx+=self.speed
                if self.button.centerx>r[self.index][0]:
                    self.button.centerx=r[self.index][0]
            if self.button.centerx>r[self.index][0]:
                self.button.centerx-=self.speed
                if self.button.centerx<r[self.index][0]:
                    self.button.centerx=r[self.index][0]
            if self.button.centery<r[self.index][1]:
                self.button.centery+=self.speed
                if self.button.centery>r[self.index][1]:
                    self.button.centery=r[self.index][1]
            if self.button.centery>r[self.index][1]:
                self.button.centery-=self.speed
                if self.button.centery<r[self.index][1]:
                    self.button.centery=r[self.index][1]
        if self.button.centerx == r[self.index][0] and self.button.centery == r[self.index][1]: #if enemy arrived at temp_destination
            self.index+=1
        return False