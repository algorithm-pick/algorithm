import sys
from collections import deque


def bfs(graph, start, n):
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우
    queue = deque([start])  # 처음 좌표 넣어주기
    graph[start[0]][start[1]] = '0'  # visited의 개념으로 갈 수 없는 것을 의미하는 0으로 변경
    count = 1  # 단지에 속하는 집의 수
    while queue:
        x, y = queue.popleft()
        for z in range(4):  # 상하좌우 탐색
            xx = x + direction[z][0]
            yy = y + direction[z][1]
            if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] == '1':
                graph[xx][yy] = '0'
                count += 1
                queue.append((xx, yy))
    return count


input = sys.stdin.readline
n = int(input())
data = [list(input().rstrip()) for _ in range(n)]  # 단지 정보
result = []  # 단지에 속하는 집의 수 리스트
for i in range(n):
    for j in range(n):
        if data[i][j] == '1':  # 새로운 단지 발견시
            result.append(bfs(data, (i, j), n))

print(len(result))  # 단지 수
print(*sorted(result), sep='\n')
