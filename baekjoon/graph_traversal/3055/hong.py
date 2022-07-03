from collections import deque
import sys
input=sys.stdin.readline

R,C=map(int,input().split())
map=[list(input().strip()) for _ in range(R)]
distance=[[0]*C for _ in range(R)]  #거리 저장 
queue=deque()

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(Dx,Dy):
    while queue:
        x,y=queue.popleft()
        if map[Dx][Dy]=='S':    #비버 굴 == 고슴도치 위치 이면 return
            return distance[Dx][Dy]
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if(map[nx][ny]=='.' or map[nx][ny]=='D') and map[x][y]=='S':    #next:(비어있는곳 or 비버의 굴) and 현재:고슴도치 위치
                    map[nx][ny]='S'  #위치 이동
                    distance[nx][ny]=distance[x][y]+1   #거리+1
                    queue.append((nx,ny))
                elif (map[nx][ny]=='.' or map[nx][ny]=='S') and map[x][y]=='*': #next:(비어있는곳 or 고슴도치 위치) and 현재:물이 차있으면 
                    map[nx][ny]='*' #물 채우기 
                    queue.append((nx,ny))
                    #D...*.
                    #.X.X..
                    #....S.
                    
    return  "KAKTUS"

for x in range(R):
    for y in range(C):
        if map[x][y]=='S':  #고슴도치 위치
            queue.append((x,y))
        elif map[x][y]=='D':  #비버 굴 
            Dx,Dy=x,y

for x in range(R):
    for y in range(C):
        if map[x][y]=='*':  #물이 차있으면 
            queue.append((x,y))
            
print(bfs(Dx,Dy))         

