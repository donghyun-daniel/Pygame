import pygame
import time
import random
import math

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

    game_name_image = large_font.render('똥피하기', True, RED)
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

def character_move(event):
    global character_x,character_y
    speed=5#캐릭터 속도
    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_w:#위로
             character_y -= speed
        if event.key == pygame.K_a:#왼쪾
             character_x -= speed
        if event.key == pygame.K_s:#아래쪾
             character_y += speed
        if event.key == pygame.K_d:#오른쪽
             character_x += speed
    pygame.draw.circle(screen,BLUE,(character_x,character_y),12)

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
    print(dx*a, dy*b)
    return dx*a,dy*b

def make_ball(v):
    size=2
    dxdy=[]
    global up,down,left,right,ball
    ab=makeAB()
    for i in range(0,len(ab)):
        dx,dy=make_dxdy(ab[i][0],ab[i][1],v)
        dxdy.append([dx,dy])

    ball.append([pygame.Rect(up[0]-size/2,up[1]+10,size*2,size*2),dxdy[0][0],dxdy[0][1]])
    ball.append([pygame.Rect(down[0]-size/2,down[1]-size*2-10,size*2,size*2),dxdy[1][0],dxdy[1][0]])
    ball.append([pygame.Rect(left[0]+10,left[1]-size/2,size*2,size*2),dxdy[2][0],dxdy[2][1]])
    ball.append([pygame.Rect(right[0]-size*2-10,right[1]-size/2,size*2,size*2),dxdy[3][0],dxdy[3][1]])

def draw_ball():
    global ball, character
    for i in ball:
        pygame.draw.circle(screen,RED,(i[0].centerx,i[0].centery),i[0].width*3)
        if character.collidepoint(i[0].centerx, i[0].centery):
            return True
    return False

def move_ball():
    global ball#ball의정보
    for i in range(0,len(ball)):
        ball[i][0].centerx+=ball[i][1]
        ball[i][0].centery+=ball[i][2]
        if ball[i][0].top < 0:
            ball[i][2]=abs(ball[i][2])
        if ball[i][0].bottom > SCREEN_HEIGHT:
            ball[i][2]=-abs(ball[i][2])
        if ball[i][0].right > SCREEN_WIDTH:
            ball[i][1]=-abs(ball[i][1])
        if ball[i][0].left < 0:
            ball[i][1]*=abs(ball[i][1])

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


up=(SCREEN_WIDTH//2,0)
right=(SCREEN_WIDTH,SCREEN_HEIGHT//2)
down=(SCREEN_WIDTH//2,SCREEN_HEIGHT)
left=(0,SCREEN_HEIGHT//2)

ball=[]
cnt=0
score=0
difficulty=0

screen_num=0

while not first_screen():
    pygame.display.update()

screen_num=difficulty

character_x=SCREEN_WIDTH//2-5
character_y=SCREEN_HEIGHT//2-5
character=pygame.Rect(character_x,character_y,20,20)

while screen_num>0 and screen_num<4:
    screen.fill(WHITE)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    character_move(event)

    if cnt%50==0:
        score+=1
    print_score(score)
    if cnt%200==0:
        make_ball(difficulty*5)

    move_ball()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    character_move(event)

    if draw_ball():
        screen_num=4
        time.sleep(3)
        break

    pygame.display.update()
    clock.tick(60)
    cnt += 1

for i in range(0,1200):#맞고나서 빠바밤 해주는곳
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