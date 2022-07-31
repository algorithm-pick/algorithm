import heapq

N, D = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(D+1)]
distance = [INF for _ in range(D+1)]


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    start, dest, length = map(int, input().split())
    if dest > D:
        continue
    graph[start].append((dest, length))

dijkstra(0)
print(distance[-1])
