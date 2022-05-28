import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs(graph, start, n, m):
    # graph : 미로 정보
    # start : 시작 좌표
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우 방향
    visited = defaultdict(int)  # 좌표별 최소 이동 거리 저장 용
    queue = deque([start])
    visited[start] = 1
    while queue:
        x, y = queue.popleft()  # 현재 좌표
        if graph[x][y] == 1:    # 이동할 수 있는 칸인가?
            for x2, y2 in d:    # 상하좌우 탐색
                x3, y3 = x + x2, y + y2     # 상하좌우 좌표
                if 0 <= x3 < n and 0 <= y3 < m:  # 갈 수 있는 상하좌우인가?
                    if visited[(x3, y3)] == 0:  # 방문하지 않았던 좌표인가?
                        visited[(x3, y3)] = visited[(x, y)] + 1  # 최소 이동거리 저장
                        queue.append((x3, y3))
    return visited[(n - 1, m - 1)]  # 도착지까지의 최소 이동 칸 수


n, m = map(int, input().split())    # n : 행 size, m : 열 size
data = [list(map(int, input().rstrip())) for _ in range(n)]  # 미로 정보

print(bfs(data, (0, 0), n, m))
