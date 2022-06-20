import sys
from collections import deque

color = dict()
color['YR'] = ['R', 'G']
color['YG'] = ['R', 'G']
color['YB'] = ['B']
color['NR'] = ['R']
color['NG'] = ['G']
color['NB'] = ['B']

def bfs(graph, visited, v, n, check):
    queue = deque([v])
    x, y = v
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        temp = queue.popleft()
        x, y = temp
        current = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and graph[nx][ny] in color[check+current]:
                queue.append((nx, ny))
                visited[nx][ny] = True

def solution():
    input = sys.stdin.readline
    n = int(input())
    graph = []
    visited_yes = [[False] * n for _ in range(n)]
    visited_no = [[False] * n for _ in range(n)]
    answer_yes = 0
    answer_no = 0
    for _ in range(n):
        temp = input()
        graph.append(list(temp.strip()))
    for a in range(n):
        for b in range(n):
            if not visited_yes[a][b]:
                bfs(graph, visited_yes, (a, b), n, 'Y')
                answer_yes += 1
            if not visited_no[a][b]:
                bfs(graph, visited_no, (a, b), n, 'N')
                answer_no += 1
    print(answer_no, end=" ")
    print(answer_yes)

solution()