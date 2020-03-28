import pygame
import time
import random
import math

pygame.display.set_caption("Avoid Ball!")

class Character(pygame.sprite.Sprite): #캐릭터 class
    def __init__(self, start_pos, up_key, down_key, left_key, right_key, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("character.png").convert_alpha(),(50,50))
        self.rect = self.image.get_rect(center=start_pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.up_key, self.down_key, self.left_key, self.right_key = up_key, down_key, left_key, right_key
        self.speed=speed
    def update(self, pressed):
        if pressed[self.up_key]:   self.rect.move_ip(0, -self.speed)
        if pressed[self.down_key]: self.rect.move_ip(0,  self.speed)
        if pressed[self.left_key]: self.rect.move_ip(-self.speed, 0)
        if pressed[self.right_key]: self.rect.move_ip(self.speed, 0)
        # keep the paddle inside the screen
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())

    def draw(self, surface):
        screen.blit(self.image,self.rect.center)

class Ball(pygame.sprite.Sprite): #Ball 클래스
    def __init__(self, start_pos, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Ball.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=start_pos)
        pygame.draw.circle(self.image, pygame.color.Color('White'), self.image.get_rect().center, 10)
        self.mask = pygame.mask.from_surface(self.image)
        # the vector we use to move the ball
        self.move_v = (dx,dy)
        # store the absolute position in self.pos
        # because a rect can only use integers
        self.pos = self.rect.center
    def update(self, dx, dy):
        # check if the ball collides with any other sprite
        collide = [s for s in pygame.sprite.spritecollide(self, self.groups()[0], False, pygame.sprite.collide_mask) if s != self]
        if collide:
            # warning: this does not handle the case of the ball hits
            # the top or bottom of the paddle, only the sides.
            self.move_v = [-self.move_v[0], self.move_v[1]]

        self.rect.move_ip(self.move_v)

def first_screen(): #첫번쨰화면
    global difficulty
    screen.fill(WHITE)  # 단색으로 채워 화면 지우기
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()

    pygame.draw.rect(screen, GREY, game_name_button)
    pygame.draw.rect(screen, BLUE, easy_button)
    pygame.draw.rect(screen, BLUE, normal_button)
    pygame.draw.rect(screen, BLUE, hard_button)

    game_name_image = large_font.render('Avoid Ball!', True, RED)
    screen.blit(game_name_image, game_name_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT * (1 / 6)))
    easy_image = small_font.render('EASY', True, RED)
    screen.blit(easy_image, easy_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT * (3 / 6)))
    normal_image = small_font.render('NORMAL', True, RED)
    screen.blit(normal_image, normal_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT * (4 / 6)))
    hard_image = small_font.render('HARD', True, RED)
    screen.blit(hard_image, hard_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT * (5 / 6)))

    if easy_button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, YELLOW, easy_button)
        easy_image = small_font.render('EASY', True, BLUE)
        screen.blit(easy_image, easy_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT * (3 / 6)))
        if event.type == pygame.MOUSEBUTTONDOWN:
            difficulty = 1

    if normal_button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, YELLOW, normal_button)
        normal_image = small_font.render('NORMAL', True, BLUE)
        screen.blit(normal_image, normal_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT * (4 / 6)))
        if event.type == pygame.MOUSEBUTTONDOWN:
            difficulty = 2

    if hard_button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, YELLOW, hard_button)
        hard_image = small_font.render('HARD', True, BLUE)
        screen.blit(hard_image, hard_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT * (5 / 6)))
        if event.type == pygame.MOUSEBUTTONDOWN:
            difficulty = 3
    return difficulty

def print_score(score):#스코어변수는 인티져타입,오른쪽위점수띄ㅓㅇ줌
    score_image = large_font.render('{}점'.format(score), True, BLACK)
    screen.blit(score_image, score_image.get_rect(right=SCREEN_WIDTH - 10, top=10))

def makeAB():
    AB=[]
    a = random.randint(-7, 7)  # 위
    b = 8 - abs(a)
    AB.append([a, b])
    a = random.randint(-7, 7)  # 아래
    b = -(8 - abs(a))
    AB.append([a, b])
    b=random.randint(-7,7)#왼쪽
    a=8-abs(b)
    AB.append([a,b])
    b=random.randint(-7,7)#오른쪽
    a=-(8-abs(b))
    AB.append([a,b])
    return AB

def make_dxdy(a,b,v):
    dx = round(math.sqrt((v * abs(a)) / (abs(a) + abs(b))),2)
    dy = round(math.sqrt((v * abs(b)) / (abs(a) + abs(b))),2)
    if a>0: a=1
    elif a<0: a=-1
    if b>0: b=1
    elif b<0: b=-1
    return dx*a,dy*b

def make_ball(v):
    global rand_pos,ball
    ab=makeAB()
    for i in range(0,len(ab)):
        dx,dy=make_dxdy(ab[i][0],ab[i][1],v)
        ball.append(Ball(random.choice(rand_pos),dx,dy))

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (100,100,100)

large_font = pygame.font.SysFont('malgungothic', 60)
small_font = pygame.font.SysFont('malgungothic', 20)

game_name_button=pygame.Rect(SCREEN_WIDTH //2-150, SCREEN_HEIGHT*(1/6)-50 ,300,100)
easy_button=pygame.Rect(SCREEN_WIDTH //2-75, SCREEN_HEIGHT*(3/6)-25 ,150,50)
normal_button=pygame.Rect(SCREEN_WIDTH //2-75, SCREEN_HEIGHT*(4/6)-25 ,150,50)
hard_button=pygame.Rect(SCREEN_WIDTH //2-75, SCREEN_HEIGHT*(5/6)-25 ,150,50)


rand_pos=[[SCREEN_WIDTH//2,0],[SCREEN_WIDTH,SCREEN_HEIGHT//2],[SCREEN_WIDTH//2,SCREEN_HEIGHT],[0,SCREEN_HEIGHT//2]]

cnt=0
score=0
difficulty=0

screen_num=0

while not first_screen():
    pygame.display.update()

screen_num=difficulty

character = Character((SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d,5)
ball=[]
make_ball(difficulty*3)
sprites=pygame.sprite.Group(character,ball)

while screen_num>0 and screen_num<4:
    screen.fill(WHITE)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    event=pygame.key.get_pressed()
    character.update(event)
    character.draw(screen)
    if cnt%50==0:
        score+=1
    print_score(score)
    if cnt%200==0:
        make_ball(difficulty*3)

    event = pygame.key.get_pressed()
    character.update(event)
    character.draw(screen)
    pygame.display.update()
    clock.tick(60)
    cnt += 1

for i in range(0,1200):
    draw_ball()
    pygame.draw.circle(screen, BLACK, (character_x, character_y), i//2)
    pygame.display.update()


while screen_num==4:
    screen.fill(BLACK)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    score_image = large_font.render('{}점'.format(score), True, WHITE)
    screen.blit(score_image, score_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2 +50))
    gmover_image = large_font.render('GAME OVER', True, WHITE)
    screen.blit(gmover_image,gmover_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=(SCREEN_HEIGHT // 2)-50))
    pygame.display.update()

pygame.quit()