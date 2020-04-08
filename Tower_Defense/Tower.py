import pygame
import Definition
import math

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (50,50,50)
S_WIDTH, S_HEIGHT = 1200, 800

tower_price=[[30,60,120],
             [50,100,200],
             [100,200,400]]
tower_range=[[300, 310, 320],
             [100, 110, 120],
             [400, 420, 440]]

class Button():
    def __init__(self, pos_x, pos_y, w, h):
        self.width, self.height = w, h
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.button=pygame.Rect(0,0,self.width,self.height)
        self.button.center=(self.pos_x,self.pos_y)
        self.font=False
        self.image=False

    def draw(self, s):
        pygame.draw.rect(s,GREY, self.button)
        if self.font:
            s.blit(self.font,self.font.get_rect(centerx=self.pos_x, centery=self.pos_y))
        if self.image:
            s.blit(self.image, self.button.topleft)

    def check_click(self, mouse_pos, event, screen):
        if self.button.collidepoint(mouse_pos):
            if self.font:
                self.font = pygame.font.SysFont('georgia', self.font_size).render(self.txt, True, BLUE)
                screen.blit(self.font, self.font.get_rect(centerx=self.pos_x, centery=self.pos_y))
            for e in event:
                if e.type==pygame.MOUSEBUTTONDOWN:
                    return self
        else:
            if self.font:
                self.font = pygame.font.SysFont('georgia', self.font_size).render(self.txt, True, RED)
                screen.blit(self.font, self.font.get_rect(centerx=self.pos_x, centery=self.pos_y))

    def add_txt(self, font_size, txt):
        self.txt = txt
        self.font_size = font_size
        self.font = pygame.font.SysFont('georgia', self.font_size).render(txt, True, RED)

    def add_image(self, image, name):
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (50,50))
        self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
        self.button.center=self.rect.center
        self.name=name


class Tower():  #range, dmg, (atk_speed is lower is better)
    def __init__(self,pos_x, pos_y):
        self.level=0
        self.type=0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.button = pygame.Rect(0, 0, 50, 50)
        self.button.center = (self.pos_x, self.pos_y)
        self.delay=0

    def upgrade(self, money, type, level):
        self.type=type
        self.level=level
        if self.type==1:
            if self.level==1:
                self.image = pygame.transform.scale(pygame.image.load("images/tower1_1.png").convert_alpha(), (50, 50))
                self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                self.button.center = self.rect.center
                self.dmg = 40
                self.atk_speed = 50
            elif self.level==2:
                self.image = pygame.transform.scale(pygame.image.load("images/tower1_2.png").convert_alpha(), (50, 50))
                self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                self.button.center = self.rect.center
                self.dmg *= 2
                self.atk_speed -= 3
            elif self.level==3:
                self.image = pygame.transform.scale(pygame.image.load("images/tower1_3.png").convert_alpha(), (50, 50))
                self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                self.button.center = self.rect.center
                self.dmg *= 2
                self.atk_speed -= 3
        elif type==2:
            if self.level==1:
                self.image = pygame.transform.scale(pygame.image.load("images/tower2_1.png").convert_alpha(), (50, 50))
                self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                self.button.center = self.rect.center
                self.dmg = 200
                self.atk_speed = 150
            if self.level==2:
                self.image = pygame.transform.scale(pygame.image.load("images/tower2_2.png").convert_alpha(), (50, 50))
                self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                self.button.center = self.rect.center
                self.dmg *= 2
                self.atk_speed -= 3
            elif self.level==3:
                self.image = pygame.transform.scale(pygame.image.load("images/tower2_3.png").convert_alpha(), (50, 50))
                self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                self.button.center = self.rect.center
                self.dmg *= 2
                self.atk_speed -= 3
        elif type==3:
            if self.level==1:
                self.image = pygame.transform.scale(pygame.image.load("images/tower3_1.png").convert_alpha(), (50, 50))
                self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                self.button.center = self.rect.center
                self.dmg = 10
                self.atk_speed = 20
            if self.level==2:
                self.image = pygame.transform.scale(pygame.image.load("images/tower3_2.png").convert_alpha(), (50, 50))
                self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                self.button.center = self.rect.center
                self.dmg *= 2
                self.atk_speed -= 3
            elif self.level==3:
                self.image = pygame.transform.scale(pygame.image.load("images/tower3_3.png").convert_alpha(), (50, 50))
                self.rect = self.image.get_rect(center=(self.button.centerx, self.button.centery))
                self.button.center = self.rect.center
                self.dmg *= 2
                self.atk_speed -= 3
        self.range = tower_range[self.type - 1][self.level - 1]



    def menu(self, mouse, event, screen, money):  # pos is the value in the map_pos
        build = []
        txt_font = pygame.font.SysFont('georgia', 20)
        pygame.draw.rect(screen, (70, 70, 70), [self.button.centerx-75, self.button.centery-75, 150, 150])
        if self.type>0:
            screen.blit(self.image, self.image.get_rect(centerx=self.button.centerx, centery=self.button.centery))

        if self.type==0:
            for i in range(4):
                build.append(Button(0, 0, 50, 50))
            build[0].button.center = (self.button.centerx + 50, self.button.centery + 50)
            build[1].button.center = (self.button.centerx - 50, self.button.centery - 50)
            build[2].button.center = (self.button.centerx + 50, self.button.centery - 50)
            build[3].button.center = (self.button.centerx - 50, self.button.centery + 50)
            Button.add_image(build[0], "images/cancel.png", "cancel")
            Button.add_image(build[1], "images/tower1_1.png", (1,1))
            Button.add_image(build[2], "images/tower2_1.png", (2,1))
            Button.add_image(build[3], "images/tower3_1.png", (3,1))

            c = txt_font.render('CANCEL', False, RED)
            t1 = txt_font.render('${}'.format(tower_price[0][0]), True, YELLOW)
            t2 = txt_font.render('${}'.format(tower_price[1][0]), True, YELLOW)
            t3 = txt_font.render('${}'.format(tower_price[2][0]), True, YELLOW)
            screen.blit(c, c.get_rect(centerx=build[0].button.centerx, centery=build[0].button.centery + 40))
            screen.blit(t1, t1.get_rect(centerx=build[1].button.centerx, centery=build[1].button.centery + 40))
            screen.blit(t2, t2.get_rect(centerx=build[2].button.centerx, centery=build[2].button.centery + 40))
            screen.blit(t3, t3.get_rect(centerx=build[3].button.centerx, centery=build[3].button.centery + 40))

        else: #tower is exists
            if self.level!=3:
                for i in range(3):
                    build.append(Button(0, 0, 50, 50))
                build[0].button.center = (self.button.centerx, self.button.centery+50)
                build[1].button.center = (self.button.centerx-50, self.button.centery-50)
                build[2].button.center = (self.button.centerx+50, self.button.centery-50)
            else:
                for i in range(2):
                    build.append(Button(0, 0, 50, 50))
                build[0].button.center = (self.button.centerx-50, self.button.centery)
                build[1].button.center = (self.button.centerx+50, self.button.centery)

            if self.type==1:
                if self.level==1:
                    Button.add_image(build[0], "images/tower1_2.png", (1,2))
                    Button.add_image(build[1], "images/cancel.png", "cancel")
                    Button.add_image(build[2], "images/sell.png", "sell")
                    c = txt_font.render('CANCEL', False, RED)
                    t1 = txt_font.render('${}'.format(tower_price[self.type-1][self.level]), True, YELLOW)
                    t2 = txt_font.render('${}'.format(int(tower_price[self.type-1][self.level-1]*0.8)), True, YELLOW)
                    screen.blit(t2, t2.get_rect(centerx=build[2].button.centerx, centery=build[2].button.centery + 40))
                    screen.blit(c, c.get_rect(centerx=build[1].button.centerx, centery=build[1].button.centery + 40))
                    screen.blit(t1, t1.get_rect(centerx=build[0].button.centerx, centery=build[0].button.centery + 40))
                elif self.level==2:
                    Button.add_image(build[0], "images/tower1_3.png", (1,3))
                    Button.add_image(build[1], "images/cancel.png", "cancel")
                    Button.add_image(build[2], "images/sell.png", "sell")
                    c = txt_font.render('CANCEL', False, RED)
                    t1 = txt_font.render('${}'.format(tower_price[self.type - 1][self.level]), True, YELLOW)
                    t2 = txt_font.render('${}'.format(int(tower_price[self.type-1][self.level-1]*0.8)), True, YELLOW)
                    screen.blit(t2, t2.get_rect(centerx=build[2].button.centerx, centery=build[2].button.centery + 40))
                    screen.blit(c, c.get_rect(centerx=build[1].button.centerx, centery=build[1].button.centery + 40))
                    screen.blit(t1, t1.get_rect(centerx=build[0].button.centerx, centery=build[0].button.centery + 40))
                elif self.level==3:
                    Button.add_image(build[0], "images/cancel.png", "cancel")
                    Button.add_image(build[1], "images/sell.png", "sell")
                    c = txt_font.render('CANCEL', False, RED)
                    t2 = txt_font.render('${}'.format(int(tower_price[self.type-1][self.level-1]*0.8)), True, YELLOW)
                    screen.blit(c, c.get_rect(centerx=build[0].button.centerx, centery=build[0].button.centery + 40))
                    screen.blit(t2, t2.get_rect(centerx=build[1].button.centerx, centery=build[1].button.centery + 40))
            elif self.type==2:
                if self.level==1:
                    Button.add_image(build[0], "images/tower2_2.png", (2,2))
                    Button.add_image(build[1], "images/cancel.png", "cancel")
                    Button.add_image(build[2], "images/sell.png", "sell")
                    c = txt_font.render('CANCEL', False, RED)
                    t1 = txt_font.render('${}'.format(tower_price[self.type - 1][self.level]), True, YELLOW)
                    t2 = txt_font.render('${}'.format(int(tower_price[self.type-1][self.level-1]*0.8)), True, YELLOW)
                    screen.blit(t2, t2.get_rect(centerx=build[2].button.centerx, centery=build[2].button.centery + 40))
                    screen.blit(c, c.get_rect(centerx=build[1].button.centerx, centery=build[1].button.centery + 40))
                    screen.blit(t1, t1.get_rect(centerx=build[0].button.centerx, centery=build[0].button.centery + 40))
                elif self.level==2:
                    Button.add_image(build[0], "images/tower2_3.png", (2,3))
                    Button.add_image(build[1], "images/cancel.png", "cancel")
                    Button.add_image(build[2], "images/sell.png", "sell")
                    c = txt_font.render('CANCEL', False, RED)
                    t1 = txt_font.render('${}'.format(tower_price[self.type - 1][self.level]), True, YELLOW)
                    t2 = txt_font.render('${}'.format(int(tower_price[self.type-1][self.level-1]*0.8)), True, YELLOW)
                    screen.blit(t2, t2.get_rect(centerx=build[2].button.centerx, centery=build[2].button.centery + 40))
                    screen.blit(c, c.get_rect(centerx=build[1].button.centerx, centery=build[1].button.centery + 40))
                    screen.blit(t1, t1.get_rect(centerx=build[0].button.centerx, centery=build[0].button.centery + 40))
                elif self.level==3:
                    Button.add_image(build[0], "images/cancel.png", "cancel")
                    Button.add_image(build[1], "images/sell.png", "sell")
                    c = txt_font.render('CANCEL', False, RED)
                    t2 = txt_font.render('${}'.format(int(tower_price[self.type-1][self.level-1]*0.8)), True, YELLOW)
                    screen.blit(c, c.get_rect(centerx=build[0].button.centerx, centery=build[0].button.centery + 40))
                    screen.blit(t2, t2.get_rect(centerx=build[1].button.centerx, centery=build[1].button.centery + 40))
            elif self.type==3:
                if self.level==1:
                    Button.add_image(build[0], "images/tower3_2.png", (3,2))
                    Button.add_image(build[1], "images/cancel.png", "cancel")
                    Button.add_image(build[2], "images/sell.png", "sell")
                    c = txt_font.render('CANCEL', False, RED)
                    t1 = txt_font.render('${}'.format(tower_price[self.type - 1][self.level]), True, YELLOW)
                    t2 = txt_font.render('${}'.format(int(tower_price[self.type-1][self.level-1]*0.8)), True, YELLOW)
                    screen.blit(t2, t2.get_rect(centerx=build[2].button.centerx, centery=build[2].button.centery + 40))
                    screen.blit(c, c.get_rect(centerx=build[1].button.centerx, centery=build[1].button.centery + 40))
                    screen.blit(t1, t1.get_rect(centerx=build[0].button.centerx, centery=build[0].button.centery + 40))
                elif self.level==2:
                    Button.add_image(build[0], "images/tower3_3.png", (3,3))
                    Button.add_image(build[1], "images/cancel.png", "cancel")
                    Button.add_image(build[2], "images/sell.png", "sell")
                    c = txt_font.render('CANCEL', False, RED)
                    t1 = txt_font.render('${}'.format(tower_price[self.type - 1][self.level]), True, YELLOW)
                    t2 = txt_font.render('${}'.format(int(tower_price[self.type-1][self.level-1]*0.8)), True, YELLOW)
                    screen.blit(t2, t2.get_rect(centerx=build[2].button.centerx, centery=build[2].button.centery + 40))
                    screen.blit(c, c.get_rect(centerx=build[1].button.centerx, centery=build[1].button.centery + 40))
                    screen.blit(t1, t1.get_rect(centerx=build[0].button.centerx, centery=build[0].button.centery + 40))
                elif self.level==3:
                    Button.add_image(build[0], "images/cancel.png", "cancel")
                    Button.add_image(build[1], "images/sell.png", "sell")
                    c = txt_font.render('CANCEL', False, RED)
                    t2 = txt_font.render('${}'.format(int(tower_price[self.type-1][self.level-1]*0.8)), True, YELLOW)
                    screen.blit(c, c.get_rect(centerx=build[0].button.centerx, centery=build[0].button.centery + 40))
                    screen.blit(t2, t2.get_rect(centerx=build[1].button.centerx, centery=build[1].button.centery + 40))

        for b in build:
            Button.draw(b,screen)
            clicked_button = Button.check_click(b,mouse,event,screen)
            if b.button.collidepoint(mouse):
                if b.name!="cancel" and b.name!="sell":
                    pygame.draw.circle(screen, (100,200,100), self.button.center, tower_range[b.name[0]-1][b.name[1]-1], 1)
            Tower.check_mouse_on(b,mouse,screen)
            if clicked_button == b:
                if clicked_button.name=="sell":
                    money+=int(tower_price[self.type-1][self.level-1]*0.8)
                    self.type=0
                    return money
                elif clicked_button.name=="cancel":
                    return money
                else:#some tower has been built
                    if money>=tower_price[clicked_button.name[0]-1][clicked_button.name[1]-1]:
                        Tower.upgrade(self, money, clicked_button.name[0], clicked_button.name[1])
                        return money-tower_price[clicked_button.name[0]-1][clicked_button.name[1]-1]
        return False


    def check_mouse_on(self, mouse, screen):
        if self.button.collidepoint(mouse):
            pygame.draw.rect(screen, (255, 255, 0), self.button, 4)

    def tower_attack(self, enemy):
        for e in enemy:
            dist= int(math.sqrt((self.button.centerx-e.button.centerx)*(self.button.centerx-e.button.centerx) + (self.button.centery-e.button.centery)*(self.button.centery-e.button.centery)))
            if dist<=self.range: #target is in the range
                if self.delay%self.atk_speed==0:
                    e.hp-=self.dmg
                    self.delay = 0
                    if e.hp<=0: # if enemy killed
                        return e.gold
                    break
