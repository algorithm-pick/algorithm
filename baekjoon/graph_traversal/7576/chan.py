from collections import deque

m, n = map(int, input().split())

# 동 남 서 북
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(graph, visit_queue):
    # 큐가 들어있는 배열 정의

    result = 0
    # while visit_queue
    while queue:
        x, y = queue.popleft()

        # 동남서북 기준
        for dx, dy in directions:
            # 막혀있으면
            xx = x + dx
            yy = y + dy

            # 예외처리
            if xx < 0 or xx > n or yy < 0 or yy > m:
                continue

            # 벽 or 예외처리
            elif graph[xx][yy] in [-1, 1]:
                continue

            # 기존에 1이라면
        result += 1

    print(result)


graph = []
initial_visited = []
visit_queue = []

for i in range(n):
    data = list(map(int, input().split()))

    for index, j in enumerate(data):
        if j == 1:
            initial_visited.append((i, index))

    graph.append(data)

for initial in initial_visited:
    visit_queue.append(deque([initial]))


bfs(graph, visit_queue)
