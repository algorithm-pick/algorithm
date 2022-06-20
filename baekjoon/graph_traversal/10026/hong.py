#bfs

N=int(input())
graph=[[]*N for _ in range(N)]

for i in range(N):
    graph[i]=list(map(int,input().split()))

def bfs():
