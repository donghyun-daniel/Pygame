import pygame

class Enemy():
    def __init__(self, pos_x, pos_y, speed, hp, gold):
        self.speed=speed
        self.hp=hp
        self.gold=gold
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.button = pygame.Rect(0, 0, self.width, self.height)
        self.button.center = (self.pos_x, self.pos_y)
    def draw_Enemy(self, screen):


def dest(i,j,dir,l):
    ans=0
    print(i,j,dir)
    if l[i][j]==2:
        return False
    if j-1>=0 and dir!=2:
        left = [l[i][j - 1], i, j-1,4]
        if left[0]:
            ans=left
    if j+1<=len(l[0]) and dir!=4:
        right = [l[i][j + 1],i,j+1,2]
        if right[0]:
            ans=right
    if i+1<=len(l[0]) and dir!=1:
        down = [l[i + 1][j],i+1,j,3]
        if down[0]:
            ans=down
    if i-1>=0 and dir!=3:
        up = [l[i - 1][j],i-1,j,1]
        if up[0]:
            ans=up
    return ans