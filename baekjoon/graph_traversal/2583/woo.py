from collections import deque
import sys

def bfs(graph, v, n, m):
    queue = deque([v])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    graph[v[0]][v[1]] = 1
    answer = 1
    while queue:
        temp = queue.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1
                answer += 1
    return answer

def solution():
    input = sys.stdin.readline
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    answer = 0
    area = []
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for a in range(y1, y2):
            for b in range(x1, x2):
                graph[a][b] = 1
    for a in range(m):
        for b in range(n):
            if graph[a][b] == 0:
                area.append(bfs(graph, (a, b), n, m))
                answer += 1
    area.sort()
    print(answer)
    print(*area)

solution()