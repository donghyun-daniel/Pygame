import pygame
import time
import random
import math

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)
pygame.display.set_caption("Avoid Ball!")

class Character(pygame.sprite.Sprite): #캐릭터 class
    def __init__(self, start_pos, up_key, down_key, left_key, right_key, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("images/Character.png").convert_alpha(),(50,50))
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
        screen.blit(self.image, self.rect.center)

class Ball(pygame.sprite.Sprite): #Ball 클래스
    global ball, difficulty, character
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("images/Ball.png").convert_alpha(),(30,30))
        start1=(random.randint(0,SCREEN_WIDTH),0)
        start2=(0,random.randint(0,SCREEN_HEIGHT))
        start3=(random.randint(0,SCREEN_WIDTH),SCREEN_HEIGHT)
        start4=(SCREEN_WIDTH,random.randint(0,SCREEN_HEIGHT))
        self.rect = self.image.get_rect(topleft=random.choice([start1,start2,start3,start4]))
        self.mask = pygame.mask.from_surface(self.image)
        rand_ab=random.choice([(2,3),(2,2),(1,4)])
        rand_sign=[-1,1]
        self.dx,self.dy=rand_ab[0]*random.choice(rand_sign), rand_ab[1]*random.choice(rand_sign)
        self.dx*=random.choice(rand_sign)
        self.dy*=random.choice(rand_sign)
        ball.add(self)

    def update(self):
        if self.rect.center[0]<0: #왼쪽 나갔을때
            self.dx=abs(self.dx)
        if self.rect.center[0]>SCREEN_WIDTH-30: #오른쪽 나갔을때
            self.dx=-abs(self.dx)
        if self.rect.center[1]<0: #위쪽 나갔을때
            self.dy=abs(self.dy)
        if self.rect.center[1]>SCREEN_HEIGHT-30: #아래쪽 나갔을때
            self.dy=-abs(self.dy)
        self.rect.move_ip(self.dx, self.dy)
        screen.blit(self.image, self.rect.center)
        return False

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

cnt=0
score=0
difficulty=0

screen_num=0

while not first_screen():
    pygame.display.flip()

screen_num=difficulty

character = Character((SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, 3)
ball=pygame.sprite.Group()

while screen_num>0 and screen_num<4:
    screen.fill(WHITE)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    event=pygame.key.get_pressed()
    character.update(event)

    if cnt%30==0:
        score+=1
    print_score(score)

    if cnt%500==0:
        for i in range(difficulty*2):
            Ball()
    character.update(event)

    for i in ball:
        Ball.update(i)
        if pygame.sprite.collide_mask(character, i):
            print("crashed")
            screen_num=4
            break

    pygame.display.flip()
    clock.tick(80)
    cnt += 1

for i in ball:
    Ball.update(i)
oops = large_font.render('OOPS!!', True, RED)
screen.blit(oops, oops.get_rect(centerx=character.rect.center[0]+30, centery=character.rect.center[1]-30))
pygame.display.update()
time.sleep(3)

while screen_num==4:
    screen.fill(BLACK)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    score_image = large_font.render('{}점'.format(score), True, WHITE)
    screen.blit(score_image, score_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2 +50))
    gmover_image = large_font.render('GAME OVER', True, WHITE)
    screen.blit(gmover_image,gmover_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=(SCREEN_HEIGHT // 2)-50))
    pygame.display.update()

pygame.quit()