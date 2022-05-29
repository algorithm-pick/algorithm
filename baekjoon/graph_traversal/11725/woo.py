from collections import defaultdict, deque

def bfs(graph, visited, v, parent):
    queue = deque([v])
    visited[v] = True
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                parent[i] = temp
                visited[i] = True

def solution():
    n = int(input())
    graph = defaultdict(list)
    visited = defaultdict(bool)
    parent = defaultdict(int)
    for _ in range(n-1):
        temp1, temp2 = map(int, input().split())
        graph[temp1].append(temp2)
        graph[temp2].append(temp1)
    bfs(graph, visited, 1, parent)
    for i in range(2, n+1):
        print(parent[i])

solution()