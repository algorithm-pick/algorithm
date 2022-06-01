# 7576 : 토마토
import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())  # m : 가로, n : 세로
queue = deque()
arr = list()  # 토마토 정보
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:  # 익은 토마토라면
            queue.append((i, j))
    arr.append(temp)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우

while queue:  # bfs 수행
    x, y = queue.popleft()
    for i, j in directions:  # 상하좌우 탐색
        xx = x + i
        yy = y + j
        if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 0:  # 익힐 수 있는 토마토라면
            arr[xx][yy] = arr[x][y] + 1
            queue.append((xx, yy))
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, arr[i][j])
print(result - 1)
