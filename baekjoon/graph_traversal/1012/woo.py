from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited, x, y):
    visited[x][y] = True
    queue = deque([(x, y)])
    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

def solution():
    t = int(input())
    for _ in range(t):
        answer = 0
        m, n, k = map(int, input().split())
        graph = [[0] * (m+2) for _ in range(n+2)]
        visited = [[False] * (m+2) for _ in range(n+2)]
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y+1][x+1] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if not visited[i][j] and graph[i][j] == 1:
                    bfs(graph, visited, i, j)
                    answer += 1
        print(answer)

solution()