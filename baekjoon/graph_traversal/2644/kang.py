# 2644 : 촌수 계산
import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n = int(input())  # 전체 사람 수
a, b = map(int, input().split())
graph = defaultdict(list)
visited = [0] * (n + 1)  # 촌수와 방문여부 표시

for _ in range(int(input())):
    d1, d2 = map(int, input().split())
    graph[d1].append(d2)
    graph[d2].append(d1)

queue = deque([a])
visited[a] = 1
while queue:  # bfs 수행
    node = queue.popleft()
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = visited[node] + 1
            queue.append(i)
    if visited[b] != 0:  # b에 도달했다면
        print(visited[b] - 1)
        exit(0)
print(-1)
