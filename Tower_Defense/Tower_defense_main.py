import pygame
import time
import random
from Button import *
from Screen import *
from Definition import *
from Tower import *
from Enemy import *

def check_area(mouse_pos, m, m_p, screen, event): #draw on the selected area, if user click on avilable area
    i = mouse_pos[1] // 50 - 2
    j=mouse_pos[0]//50-2
    if m[i][j]==0:
        pygame.draw.rect(screen,(255,255,0),[m_p[i][j][0]-25,m_p[i][j][1]-25,50,50])
        for e in event:
            if e.type == pygame.MOUSEBUTTONDOWN:
                return (m_p[i][j][0], m_p[i][j][1])
            else:
                return False
    return False

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
buttons.append(pause)
isPause=False
money, score, life = 100, 0, 100
build_state, where_click= False, False # "where" is the pos where the mouse click on avail place
cnt=-1

#build button
build=[]
for i in range(4):
    build.append(Button(0,0, 50, 50))

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
    for e in event:
        if e.type == pygame.QUIT:
            pygame.quit()

    if isPause: #if Pause, just only do this
        pygame.display.flip()
        for b in buttons:  # check which button is clicked
            Button.draw(b, game_screen.screen)
            a = Button.check_click(b, pygame.mouse.get_pos(), event, game_screen.screen)
            if a == pause:  # if user click pause
                isPause = not (isPause)
    else:
        Screen.draw_values(first_screen, money, score, life, stage_index, 40)

        mouse = pygame.mouse.get_pos() #get mouse position
        print_map(map, map_pos, game_screen.screen)

        event = pygame.event.get()  # get event
        for e in event:
            if e.type == pygame.QUIT:
                pygame.quit()

        for b in buttons: #draw and check which button is clicked
            Button.draw(b,game_screen.screen)
            a = Button.check_click(b, pygame.mouse.get_pos(), event, game_screen.screen)
            if a==pause: #if user click pause
                isPause = not(isPause)
        """
        if (100<=mouse[0] and mouse[0]<1100) and (100<=mouse[1] and mouse[1] < 700) and not build_state:  #if mouse is on the map
            where = check_area(mouse, map, map_pos, game_screen.screen, event)
            if where and not build_state: #user click on build available area, do build
                build_state=True
                build[0].button.center=(where[0]+50, where[1]+50)
                build[1].button.center=(where[0]-50, where[1]-50)
                build[2].button.center = (where[0]+50, where[1]-50)
                build[3].button.center = (where[0]-50, where[1]+50)
                Button.add_image(build[0], "images/cancel.png")
                Button.add_image(build[1], "images/tower1_1.png")
                Button.add_image(build[2], "images/tower2_1.png")
                Button.add_image(build[3], "images/tower3_1.png")

        if build_state:
            which=build_towers(build, mouse, event, game_screen.screen)
            if which == build[0]: #if click cancel button
                print("Cancel")
                build_state = False
            elif which == build[1]:
                print("11")
                build_state = False
                #build tower1
            elif which == build[2]:
                print("22")
                build_state = False
                # build tower2
            elif which == build[3]:
                print("33")
                build_state = False
                # build tower3
                """
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
            if Enemy.move_Enemy(E[i], route):
                del E[i]
                i -= 1
            else:
                Enemy.draw_Enemy(E[i],game_screen.screen)
            i+=1



        clock.tick(80)
        pygame.display.flip()
        cnt+=1 #Time flows....

pygame.quit()
