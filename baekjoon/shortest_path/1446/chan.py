import sys
import heapq

N, D = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(D + 1)]

for i in range(D):
    graph[i].append((i + 1, 1))

for i in range(N):
    start, end, short = map(int, sys.stdin.readline().split())
    if end > D:
        continue
    graph[start].append((end, short))

INF = 1e9
distance = [INF] * (D + 1)
distance[0] = 0

q = []
heapq.heappush(q, (0, 0))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for x in graph[now]:
        cost = dist + x[1]

        if distance[x[0]] > cost:
            distance[x[0]] = cost
            heapq.heappush(q, (cost, x[0]))

print(distance[D])
