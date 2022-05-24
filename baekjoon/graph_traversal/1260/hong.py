from collections import deque 

n,m,v= map(int, input().split())

graph=[[]*n for _ in range(n+1)]

for i in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs_recursive(graph, start, visited=[]):
    visited.append(start)
    
    graph[start].sort()
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

def bfs(graph,start,visited):
    queue=deque([start]) #시작 노드 넣어줌 
    visited[start]=True #시작노드 방문 처리 
    
    while queue:   #queue 가 빌 때까지 
        v=queue.popleft()   
        print(v, end=' ')   #가장 먼저 들어온 원소 출력
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


arr=dfs_recursive(graph,v)
for i in range(len(arr)):
    print(arr[i], end=' ')

print("")
bfs(graph, v,visited=[0]*(n+1))   
