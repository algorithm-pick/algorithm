import sys
sys.setrecursionlimit(10**6)

N=int(input())
graph=graph=[[]*N for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited=[0]*(N+1)

def dfs(k):
    for i in graph[k]:
        if visited[i]==0:
            visited[i]=k
            dfs(i)

dfs(1) 

for i in range(2, N+1):
    print(visited[i])
