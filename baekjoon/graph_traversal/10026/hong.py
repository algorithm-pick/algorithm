#bfs
from collections import deque

N=int(input())
graph=[[]*N for _ in range(N)]
visited=[[False]*N for _ in range(N)]

for i in range(N):
    graph[i]=list(map(str,input().split()))


dx = [1, 0, -1, 0]  # 아래, 오른, 왼, 위
dy = [0, 1, 0, -1]       

def bfs(x,y,color):
    queue=deque()
    queue.append((x,y)) 
    
    while queue:
        x,y=queue.popleft()
        
        if visited[x][y]==False:
            visited[x][y]=True
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if graph[nx][ny]==color:
                        queue.append((nx,ny))
             
#Not
cnt=0
for i in range(N):
     for j in  range(N):
         if visited[i][j]==False: #not visited
             color=graph[i][j]
             bfs(i,j,color)
             cnt+=1
             
#Is 
visited=[[False]*N for _ in range(N)]  
for i in range(N):
     for j in  range(N):
         if visited[i][j]=='G':
             visited[i][j]='R'
             
cnt2=0
for i in range(N):
    for j in range(N):
        if visited[i][j]==False:
            color=graph[i][j]
            bfs(i,j,color)
            cnt2+=1

print(cnt)
print(cnt2)          
        
