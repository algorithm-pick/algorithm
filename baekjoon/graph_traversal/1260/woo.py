from collections import deque

def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

def bfs(graph, visited, v):
    queue = deque([v])
    visited[v] = True
    while queue:
        temp = queue.popleft()
        print(temp, end=' ')
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def solution():
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        temp1, temp2 = map(int, input().split())
        graph[temp1].append(temp2)
        graph[temp2].append(temp1)
    for i in graph:
        i.sort()
    visited = [False] * (n + 1)
    dfs(graph, visited, v)
    print()
    visited = [False] * (n + 1)
    bfs(graph, visited, v)

solution()