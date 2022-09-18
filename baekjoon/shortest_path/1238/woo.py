import sys
import heapq

INF = int(1e9)

def dijkstra(graph, start, n):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n+1)
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
    return distance

def solution():
    input = sys.stdin.readline
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    answer = [0] * (n+1)
    for _ in range(m):
        a, b, c  = map(int, input().split())
        graph[a].append((b, c))
    for i in range(1, n+1):
        dist = dijkstra(graph, i, n)
        answer[i] += dist[x]
        if i == x:
            for k in range(1, n+1):
                answer[k] += dist[k]
    print(max(answer))

solution()
