import sys
from collections import deque

def bfs(graph, visited, v, r, c):
    x, y = v
    visited[x][y] = True
    queue = deque([v])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = [0, 0] # sheep, wolf
    escape = False
    while queue:
        temp = queue.popleft()
        x, y = temp
        if graph[x][y] == 'o':
            answer[0] += 1
        if graph[x][y] == 'v':
            answer[1] += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                if graph[x][y] == '.':
                    escape = True
                continue
            if not visited[nx][ny] and graph[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
    if escape:
        return [0, 0]
    return answer

def solution():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    graph = []
    visited = [[False] * c for _ in range(r)]
    answer = [0, 0] # sheep, wolf
    for _ in range(r):
        graph.append(list(input().strip()))
    for a in range(r):
        for b in range(c):
            if not visited[a][b] and graph[a][b] != '#':
                temp = bfs(graph, visited, (a, b), r, c)
                if temp[0] > temp[1]:
                    answer[0] += temp[0]
                else:
                    answer[1] += temp[1]
    print(*answer)

solution()