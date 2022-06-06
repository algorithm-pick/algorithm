# 14502 : 연구소
# https://www.acmicpc.net/problem/14502
import sys
from collections import deque
from itertools import combinations


def bfs_and_count_zero(graph, virus_pos, n, m):  # 너비 우선 탐색 & 빈칸 수 구하기
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * m for _ in range(n)]
    for i, j in virus_pos:
        visited[i][j] = True
    queue = deque(virus_pos)

    while queue:  # 바이러스 전파하기!
        x, y = queue.popleft()
        for i in range(4):
            xx = x + directions[i][0]
            yy = y + directions[i][1]
            if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == 0:
                if not visited[xx][yy]:
                    visited[xx][yy] = True
                    queue.append((xx, yy))

    count = 0
    for i in range(n):  # 빈 칸 세기
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 0:
                count += 1
    return count


input = sys.stdin.readline
n, m = map(int, input().split())  # n : 세로, m : 가로
blank_pos, virus_pos = set(), set()  # blank_pos : 빈 칸 위치들, virus_pos : 바이러스 위치
arr = []  # 연구소 지도
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 0:  # 빈 칸인 위치라면
            blank_pos.add((i, j))
        elif temp[j] == 2:  # 바이러스가 있는 위치라면
            virus_pos.add((i, j))
    arr.append(temp)

result = 0
for a, b, c in combinations(blank_pos, 3):  # 빈 칸 위치 중 3개 뽑기
    # 빈 칸을 벽으로 만들기
    arr[a[0]][a[1]] = 1
    arr[b[0]][b[1]] = 1
    arr[c[0]][c[1]] = 1

    result = max(result, bfs_and_count_zero(arr, virus_pos, n, m))

    # 다시 빈 칸으로 변경
    arr[a[0]][a[1]] = 0
    arr[b[0]][b[1]] = 0
    arr[c[0]][c[1]] = 0

print(result)
