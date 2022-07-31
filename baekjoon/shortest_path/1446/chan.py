import sys
import heapq

N, D = map(int, sys.stdin.readline().split())
INF = 1e9

graph = [[] for _ in range(D + 1)]
distance = [INF] * (D + 1)
distance[0] = 0

for i in range(D):
    graph[i].append((i + 1, 1))

for _ in range(N):
    start, end, short = map(int, sys.stdin.readline().split())
    if end > D:
        continue
    graph[start].append((end, short))

q = []
heapq.heappush(q, (0, 0))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for j in graph[now]:
        cost = dist + j[1]

        if distance[j[0]] > cost:
            distance[j[0]] = cost
            heapq.heappush(q, (cost, j[0]))

print(distance[D])
