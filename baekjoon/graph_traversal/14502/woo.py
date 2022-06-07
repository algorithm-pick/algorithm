from collections import deque
from itertools import combinations
import copy

def bfs(graph, v):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([v])
    while queue:
        temp = queue.popleft()
        x, y = temp
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))

def solution():
    n, m = map(int, input().split())
    graph = [[1] * (m+2) for _ in range(n+2)]
    for i in range(1, n+1):
        graph[i][1:m+1] = list(map(int, input().split()))
    zero = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            if graph[i][j] == 0:
                zero.append((i, j))
    combin = list(combinations(zero, 3)) # 조합 구하기
    answer = []
    for i in combin:
        temp = copy.deepcopy(graph)
        for j in i:
            x, y = j
            temp[x][y] = 1
        for a in range(1, n+1):
            for b in range(1, m+1):
                if temp[a][b] == 2:
                    bfs(temp, (a, b))
        zero_sum = 0
        for a in range(1, n+1):
            for b in range(1, m+1):
                if temp[a][b] == 0:
                    zero_sum += 1
        answer.append(zero_sum)
    print(max(answer))

solution()