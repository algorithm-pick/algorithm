#bfs
from collections import deque

N,K=map(int,input().split())
graph=[[]*N for _ in range(N)]
virus=[]
for i in range(N):
    graph[i]=list(map(int,input().split()))
    for j in range(N):
        if graph[i][j]!=0:
            virus.append(((graph[i][j],i,j)))   #바이러스의 숫자, 위치 저장
s,x,y=map(int, input().split())


def bfs(s,X,Y):
    queue=deque(virus)
    sec=0

    dx = [1, 0, -1, 0]  # 아래, 오른, 왼, 위
    dy = [0, 1, 0, -1]

    while queue:
        if sec==s:
            break
        for _ in range(len(queue)):
            prev,x,y=queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N:
                   if(graph[nx][ny]==0):
                        graph[nx][ny]=graph[x][y]
                        queue.append((graph[nx][ny],nx,ny))
        sec+=1
    return graph[X-1][Y-1]

virus.sort()
print(bfs(s,x,y))
