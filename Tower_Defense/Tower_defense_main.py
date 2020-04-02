import pygame
import time
import random
from Button import *
from Screen import *
from Definition import *
from Tower import *

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

def build_tower(pos,m,e,scr): #pos is the value in the map_pos
    global build_state,tower
    tower.append(Button(pos[0],pos[1],50,50))
    tower.append(Button(pos[0], pos[1], 50, 50))
    tower.append(Button(pos[0], pos[1], 50, 50))
    tower.append(Button(pos[0], pos[1], 50, 50))
    Button.add_image(tower[0], "images/cancel.png")
    Button.add_image(tower[1], "images/tower1_1.png")
    Button.add_image(tower[2], "images/tower2_1.png")
    Button.add_image(tower[3], "images/tower3_1.png")
    for t in tower:
        Button.draw(t,game_screen.screen)
    for t in range(len(tower)):
        if (tower[0] == Button.check_click(tower[t], m, e, scr)): #if that button was cancel
            build_state=False


#map, map_pos init
map=[[1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0],#1이길 0은 설치되는곳
      [0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
      [0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0],
      [0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0],
      [0,0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,1,0,0,0],
      [0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0],
      [0,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,0],
      [0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
      [0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0],
      [0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0],
      [0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]]
map_pos=[]

for i in range(len(map)):
    map_pos.append([])
    for j in range(len(map[0])):
        map_pos[i].append((125 + (j * 50), 125 + (i * 50)))

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
tower=[]
cnt=0
while True: #Game Screen of TD
    Screen.draw_values(first_screen, money, score, life, 40)
    event = pygame.event.get() #get event
    mouse = pygame.mouse.get_pos() #get mouse position
    print_map(map, map_pos, game_screen.screen)

    for e in event:
        if e.type == pygame.QUIT:
            pygame.quit()

    for b in buttons: #check which button is clicked
        Button.draw(b,game_screen.screen)
        a = Button.check_click(b, pygame.mouse.get_pos(), event, game_screen.screen)
        if a==pause: #if user click pause
            isPause = not(isPause)

    if (100<=mouse[0] and mouse[0]<1100) and (100<=mouse[1] and mouse[1] < 700):  #if mouse is on the map
        where = check_area(mouse, map, map_pos, game_screen.screen, event)
        if where and not build_state: #user click on build available area, do build
            where_click=where
            build_state=True
    if build_state and where_click:
        build(where_click, mouse, event, game_screen.screen)



    if isPause:
        cnt-=1 #Stop time
    clock.tick(80)
    pygame.display.flip()
    cnt+=1 #Time flows....

pygame.quit()
