import sys
from collections import deque

def bfs(graph, v, m, n):
    queue = deque([v])
    visited = [[False] * n for _ in range(m)]
    x, y = v
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        temp = queue.popleft()
        x, y = temp
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m:
                return True
            if nx < 0 or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and graph[nx][ny] == '0':
                queue.append((nx, ny))
                visited[nx][ny] = True
    return False

def solution():
    input = sys.stdin.readline
    m, n = map(int, input().split())
    graph = []
    for _ in range(m):
        graph.append(list(input()))
    answer = 'NO'
    for i in range(n):
        temp = bfs(graph, (0, i), m, n)
        if temp:
            answer = 'YES'
            break
    print(answer)

solution()