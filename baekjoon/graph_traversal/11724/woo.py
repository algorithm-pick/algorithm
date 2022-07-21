import sys
from collections import defaultdict, deque

def bfs(graph, visited, v):
    queue = deque([v])
    visited[v] = True
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = defaultdict(list)
    visited = defaultdict(bool)
    answer = 0
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n+1):
        if not visited[i]:            
            bfs(graph, visited, i)
            answer += 1
    print(answer)

solution()