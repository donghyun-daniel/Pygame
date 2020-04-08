import pygame
import time
import random
from Screen import *
from Definition import *
from Tower import *
from Enemy import *

def check_area(mouse_pos, m, m_p, screen, event): #draw on the selected area, if user click on avilable area
    i = mouse_pos[1] // 50 - 2
    j=mouse_pos[0]//50-2
    if tower[i][j]:
        if tower[i][j].type==0:
            pygame.draw.rect(screen,(180,180,0),[m_p[i][j][0]-25,m_p[i][j][1]-25,50,50],4)

def print_map(m,m_p,screen): #draw available area
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==0: #if build available area
                pygame.draw.rect(screen, (100, 50, 255, 50), [m_p[i][j][0]-25, m_p[i][j][1]-25, 50, 50], 1)

def stage_enemy_small(cnt, hp, small_interval, E, s):
    if cnt%small_interval==0:
        E.append(Enemy(hp, 10, "small"))  # hp, gold, kind
        s[stage_index][0]-=1


def stage_enemy_big(cnt, hp, big_interval, E, s):
    if cnt%big_interval==0:
        E.append(Enemy(hp, 10, "big"))  # hp, gold, kind
        s[stage_index][1]-=1

#First Screen

pygame.init()
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)
pygame.display.set_caption("Tower Defense v1")
buttons=[]

start=Button(S_WIDTH//2, S_HEIGHT//3*2, 300, 100)
Button.add_txt(start, 40, "START")
buttons.append(start)
first_screen = Screen("images/background.png", 1200, 800)
game_name_txt = pygame.font.SysFont('georgia', 100).render('Tower Defense', True, WHITE)
first_screen.screen.blit(game_name_txt, game_name_txt.get_rect(centerx=S_WIDTH//2, centery=S_HEIGHT//3))

while True: #First Screen of TD
    event=pygame.event.get()
    for b in buttons:
        Button.draw(b,first_screen.screen)
    for e in event:
        if e.type == pygame.QUIT:
            pygame.quit()
    if Button.check_click(start, pygame.mouse.get_pos(), event, first_screen.screen):
        break
    pygame.display.flip()

buttons.clear() # Remove start button after first screen

#Game screen init
game_screen = Screen("images/background.png", 1200, 800)
pause=Button(40,S_HEIGHT-50, 40, 40)
Button.add_txt(pause, 40, "P")
pause_font = pygame.font.SysFont('georgia', 300)
pause_render = pause_font.render('PAUSE', True, (200, 200, 200))
isPause=False
money, score, life = 1000, 0, 100
build_state, where_click= False, False # "where" is the pos where the mouse click on avail place
build_info=0
cnt=-1

#make Enemy's list
E=[]
stage_enemy=[]#small_num, big_num
for i in range(0, 50):
    if i%3==2:
        stage_enemy.append([i * 3, i * 3])
    else:
        stage_enemy.append([i * 5 + 5, 0])
stage_index=0

while True: #Game Screen of TD
    event = pygame.event.get()  # get event
    mouse = pygame.mouse.get_pos()  # get mouse position
    for e in event:
        if e.type == pygame.QUIT:
            pygame.quit()

    # check pause button is clicked
    Button.draw(pause, game_screen.screen)
    if Button.check_click(pause, pygame.mouse.get_pos(), event, game_screen.screen)==pause:
        isPause=not(isPause)

    if isPause: #if Pause, just only do this
        game_screen.screen.blit(pause_render, pause_render.get_rect(centerx=(game_screen.width // 2), centery=game_screen.height // 2))
        Button.draw(pause, game_screen.screen)
        pygame.display.flip()


    else:
        Screen.draw_values(first_screen, money, score, life, stage_index, 40)
        Button.draw(pause, game_screen.screen)

        for i in range(len(tower)): #Show towers on the map
            for j in range(len(tower[0])):
                if tower[i][j]:
                    if tower[i][j].type>0:
                        game_screen.screen.blit(tower[i][j].image, tower[i][j].image.get_rect(centerx=tower[i][j].button.centerx, centery=tower[i][j].button.centery))
                        if tower[i][j].delay<tower[i][j].atk_speed: #manage tower atk speed
                            tower[i][j].delay+=1
                        drop_gold = Tower.tower_attack(tower[i][j], E)
                        if drop_gold:
                            money+=drop_gold
                        if tower[i][j].button.collidepoint(mouse):
                            pygame.draw.circle(game_screen.screen, (100, 200, 100), tower[i][j].button.center, tower[i][j].range, 1)



        print_map(map, map_pos, game_screen.screen)

        if (100 <= mouse[0] and mouse[0] < 1100) and (100 <= mouse[1] and mouse[1] < 700) and not build_state:
            i = mouse[1] // 50 - 2
            j = mouse[0] // 50 - 2
            if tower[i][j]:
                Tower.check_mouse_on(tower[i][j], mouse, game_screen.screen)
                for e in event:
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        build_state = True
                        build_info=(i,j)

        if build_state:
            m = Tower.menu(tower[build_info[0]][build_info[1]], mouse, event, game_screen.screen, money)
            if m:
                build_state=False
                money=m

        if cnt>=300: #stage start interval
            if stage_enemy[stage_index][0] > 0 and cnt>=500:
                stage_enemy_small(cnt, 100+(stage_index//10)*20, 10, E, stage_enemy) # cnt, hp, small_interval, big_interval, E, s
            if stage_enemy[stage_index][1] > 0:
                stage_enemy_big(cnt, 200+(stage_index//10)*50, 40, E, stage_enemy) # cnt, hp, small_interval, big_interval, E, s
            if stage_enemy[stage_index]==[0,0] and len(E)==0: #Everthing made or All enemy is dead
                cnt=0
                stage_index+=1

        #move enemy
        i=0
        while i<len(E):
            if Enemy.move_Enemy(E[i], route) or E[i].hp<=0: #if enemy arrive at end point
                if E[i].hp>0:
                    life-=(E[i].hp//20)
                del E[i]
                i -= 1
            else:
                Enemy.draw_Enemy(E[i],game_screen.screen)
            i+=1


        clock.tick(80)
        pygame.display.flip()
        cnt+=1 #Time flows....

pygame.quit()
