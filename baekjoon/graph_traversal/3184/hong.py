from collections import deque
import sys 
input=sys.stdin.readline

def bfs(x,y):
    s,w=0,0
    queue=deque()
    queue.append((x,y))
    
    while queue:   
        x,y=queue.popleft()
         
        for i in range(5):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]: #범위 안에 있고,방문하지 않은 경우 
                if graph[nx][ny]=='#':    
                    continue
                elif graph[nx][ny]=='o':
                    s+=1
                elif graph[nx][ny]=='v':
                    w+=1
                
                queue.append((nx,ny))
                visited[nx][ny]=1
        

    return s, w
    
r,c=map(int,input().split())
graph=[]
visited=[[0]*c for _ in range(r)]

for _ in range(r):
    graph.append(list(input().rstrip()))
    
dx=[1,-1,0,0,0]
dy=[0,0,1,-1,0]

sheep, wolf=0,0

for i in range(r):
    for j in range(c):
        if not visited[i][j]  and graph[i][j]!='#': #아직 방문하지 않았고, 울타리가 아니면 bfs
            s, w=bfs(i,j) 
            if s>w:
                sheep+=s
            else:
                wolf+=w
                
            
print(sheep, wolf)
