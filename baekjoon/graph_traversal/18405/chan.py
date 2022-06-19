from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

# 동 남 서 북
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(graph, start, find_second):
    queue = deque(start)

    while queue:
        x, y, second = queue.popleft()
        if second == find_second:
            break

        virus = graph[x][y]
        for dx, dy in dirs:
            xx = x + dx
            yy = y + dy
            if xx < 0 or xx >= n or yy < 0 or yy >= n:
                continue

            # 전파할 좌표에 바이러스가 있으면
            if graph[xx][yy] > 0:
                continue

            graph[xx][yy] = virus
            queue.append((xx, yy, second + 1))

    return


graph, initial_virus = [], []
for row in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    graph.append(line)
    [initial_virus.append([row, col, 0]) for col, val in enumerate(line) if val > 0]

# 순서 정렬
for i in range(0, len(initial_virus) - 1):
    x, y = initial_virus[i][0], initial_virus[i][1]

    for j in range(i + 1, len(initial_virus)):
        ax, ay = initial_virus[j][0], initial_virus[j][1]

        if graph[x][y] > graph[ax][ay]:
            temp = initial_virus[i]
            initial_virus[i] = initial_virus[i + 1]
            initial_virus[i + 1] = temp

s, x, y = map(int, sys.stdin.readline().split())
# 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다
bfs(graph, initial_virus, s + 1)

print(graph[x - 1][y - 1])
