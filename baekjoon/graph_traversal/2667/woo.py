from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited, x, y):
    visited[x][y] = 1
    queue = deque([(x, y)])
    answer = 1
    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if not visited[nx][ny] and graph[nx][ny] == '1':
                queue.append((nx, ny))
                visited[nx][ny] = True
                answer += 1
    return answer

def solution():
    answer = []
    n = int(input())
    graph = [['0'] * (n+2) for _ in range(n+2)]
    visited = [[False] * (n+2) for _ in range(n+2)]
    for i in range(1, n+1):
        graph[i][1:n+1] = list(input())
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not visited[i][j] and graph[i][j] == '1':
                answer.append(bfs(graph, visited, i, j))
    answer.sort()
    print(len(answer))
    for i in answer:
        print(i)

solution()