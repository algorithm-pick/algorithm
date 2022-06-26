import sys
from collections import deque

def bfs(graph, visited, v, n, m):
    queue = deque([v])
    x, y = v
    visited[x][y] = True
    size = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        temp = queue.popleft()
        x, y = temp
        direct = format(graph[x][y], 'b').zfill(4)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if direct[i] == '0' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                size += 1
    return size

def solution():
    input = sys.stdin.readline
    m, n = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]
    room_max_size = -1
    room_num = 0
    for a in range(n):
        for b in range(m):
            if not visited[a][b]:
                size = bfs(graph, visited, (a, b), n, m)
                room_num += 1
                if size > room_max_size:
                    room_max_size = size
    room_max_size_wall = -1
    for a in range(n):
        for b in range(m):
            visited = [[False] * m for _ in range(n)]
            bin = format(graph[a][b], 'b').zfill(4)
            for i in range(4):
                if bin[i] == '1':
                    graph[a][b] -= pow(2, 3 - i)
                    size = bfs(graph, visited, (a, b), n, m)
                    if size > room_max_size_wall:
                        room_max_size_wall = size
                    graph[a][b] += pow(2, 3 - i)
    print(room_num)
    print(room_max_size)
    print(room_max_size_wall)

solution()