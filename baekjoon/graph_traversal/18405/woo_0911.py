import sys
from collections import deque

def bfs(graph, virus, s, n):
    queue = deque(virus)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        temp = queue.popleft()
        if temp[3] == s:
            break
        for i in range(4):
            nx = temp[1] + dx[i]
            ny = temp[2] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = temp[0]
                queue.append((temp[0], nx, ny, temp[3]+1))
    return

def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    graph = []
    virus = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
        for j in range(n):
            if graph[i][j] != 0:
                virus.append((graph[i][j], i, j, 0))
    virus.sort()
    s, x, y = map(int, input().split())
    bfs(graph, virus, s, n)
    print(graph[x-1][y-1])

solution()