import pygame
from Definition import *

class Enemy():
    def __init__(self, pos_x, pos_y, speed, hp, gold, kind):
        if kind=="small":
            self.image = pygame.transform.scale(pygame.image.load("images/enenmy_small.png").convert_alpha(), (50, 50))
        elif kind=="big":
            self.image = pygame.transform.scale(pygame.image.load("images/enemy_big.png").convert_alpha(), (50, 50))
        self.speed=speed
        self.hp=hp
        self.gold=gold
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.button = pygame.Rect(0, 0, self.width, self.height)
        self.button.center = (self.pos_x, self.pos_y)
        self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
        self.button.center = self.rect.center

    def draw_Enemy(self, s):
        s.blit(self.image, self.button.topleft)

    def move_Enemy(self, dest):
        while (self.button.centerx!=dest[0] or self.button.centery!=dest[1]):
            if self.button.centerx<dest[0]:
                self.button.centerx+=self.speed
            if self.button.centerx>dest[0]:
                self.button.centerx-=self.speed
            if self.button.centery<dest[1]:
                self.button.centerx+=self.speed
            if self.button.centery>dest[1]:
                self.button.centery-=self.speed


def dest(i,j,dir,l,r):
    ans=[0,0,0,0]
    print(i,j)
    if i==len(l)-1 and j==len(l[0])-1:
        return False
    if j>=1 and dir!=2:
        left = [l[i][j - 1], i, j-1,4]
        if left[0]:
            ans=left
    if j+1<len(l[0]) and dir!=4:
        right = [l[i][j + 1],i,j+1,2]
        if right[0]:
            ans=right
    if i+1<len(l) and dir!=1:
        down = [l[i + 1][j],i+1,j,3]
        if down[0]:
            ans=down
    if i>=1 and dir!=3:
        up = [l[i - 1][j],i-1,j,1]
        if up[0]:
            ans=up

    make_dest_pos(r, ans[1], ans[2])
    return ans

def make_dest_pos(r, ans_r, ans_c):
    m = map_pos[ans_r][ans_c]
    r.append((m[0], m[1]))