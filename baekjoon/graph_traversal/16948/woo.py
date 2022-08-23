from collections import deque
import sys

def bfs(graph, v, n):
    queue = deque([v])
    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]
    graph[v[0]][v[1]] = 0
    while queue:
        temp = queue.popleft()
        for i in range(6):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == -1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[temp[0]][temp[1]] + 1

def solution():
    input = sys.stdin.readline
    n = int(input())
    r1, c1, r2, c2 = map(int, input().split())
    graph = [[-1] * n for _ in range(n)]
    bfs(graph, (r1, c1), n)
    print(graph[r2][c2])

solution()