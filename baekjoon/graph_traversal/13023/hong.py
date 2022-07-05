n,m=map(int, input().split())
graph=[[] for i in range(n)]
visited=[False]*n

for _ in range(m):
    a,b=map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
   
def dfs(idx, num):
    #그래프의 깊이가 5이면 조건 만족
    if num==4:
        print(1)
        exit()
        
    for i in graph[idx]:
        visited[i]=True
        dfs(i, num+1)
        visited[i]=False
 
#노드 순서대로 방문 하면서 dfs 
for i in range(n):
    visited[i]=True
    dfs(i,0)
    visited[i]=False
    
print(0)
    
