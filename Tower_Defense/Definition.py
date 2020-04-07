import pygame
from Tower import *

#these funcs for make route
def dest(i,j,dir,l,r):
    ans=[0,0,0,0]
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

#init some config

#Color Definition
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (50,50,50)
S_WIDTH, S_HEIGHT = 1200, 800

#map, map_pos init, 0 is build available area, 1 is road
map=[[1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
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

tower=[]
for i in range(0,len(map)):
    tower.append([])
    for j in range(len(map[0])):
        if not map[i][j]:
            tower[i].append(Tower(map_pos[i][j][0], map_pos[i][j][1]))
        else:
            tower[i].append(False)

#make route
route=[(125,125)]
ans = [0, 0, 0, 2]
while ans:
    ans = dest(ans[1], ans[2], ans[3], map, route)

