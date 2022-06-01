import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, start, m, n):
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우
    queue = deque([start])  # 처음 좌표 넣어주기
    graph[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 상하좌우 탐색
            xx = x + direction[i][0]
            yy = y + direction[i][1]
            if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == 1:  # 유효한 범위안에서 접근 가능한가?
                graph[xx][yy] = 0  # 더이상 접근할 수 없게 변경
                queue.append((xx, yy))


for _ in range(int(input())):
    # m : 가로 길이, n : 세로 길이, k : 배추 심어진 위치 수
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1
    count = 0  # 지렁이 수
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:  # 배추 발견!
                bfs(arr, (i, j), m, n)
                count += 1  # 지렁이 추가
    print(count)
