#11559
from collections import deque

graph=[]
for _ in range(12):
    graph.append(list(input()))
      
result=0

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(a,b,c):
    queue=deque()
    queue.append((a,b))
    
    blast=deque()
    blast.append((a,b))
    
    visited=[[False]*6 for _ in range(12)]  
    visited[a][b]=True
    count=1
    flag=0
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>11 or ny<0 or ny>5:
                continue
            if graph[nx][ny]==c and visited[nx][ny]==False:
                queue.append((nx,ny))
                blast.append((nx,ny))
                visited[nx][ny]=True
                count+=1
                
    if count>=4:
        flag=1
        for x,y in blast:
            graph[x][y]='.'
            
    return flag
    

def puyo(): #graph 정리
    for y in range(6):
        queue=deque()
        for x in range(11,-1,-1):
            if graph[x][y]!='.':
                queue.append(graph[x][y])
        for x in range(11,-1,-1):
            if queue:
                graph[x][y]=queue.popleft()
            else:
                graph[x][y]='.'
        
while True:
    check=0
    for i in range(12):
        for j in range(6):
            if graph[i][j]!='.':
                check+=bfs(i,j,graph[i][j])
    
    if check==0:
        print(result)
        break
    else:
        result+=1
        
    puyo()
    
