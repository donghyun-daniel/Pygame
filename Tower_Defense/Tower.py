import pygame
from Definition import *

class Tower():
    def __init__(self, type):
        self.type=type
        self.level=1
        #ramnge, dmg, atk_speed is lower is better
        if self.type==1:
            self.range=300
            self.dmg=40
            self.atk_speed=50
            self.price=30
        elif self.type==2:
            self.range=100
            self.dmg=80
            self.atk_speed=30
            self.price=40
        elif self.type==3:
            self.range=400
            self.dmg=70
            self.atk_speed=25
            self.price=100

    def upgrade(self, money):
        if money>=self.price*2 and self.level<3:
            money-=self.price*2
            self.level+=1
            self.dmg*=2
            self.atk_speed-=3

    def sell(self, money):
        money+=(int(self.price*0.8))
        del self
        return money


