from collections import defaultdict, deque

def bfs(graph, v, dist):
    visited = defaultdict(bool)
    visited[v] = True
    queue = deque([v])
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                dist[i] = dist[temp] + 1

def solution():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    graph = defaultdict(list)
    dist = defaultdict(int)
    for _ in range(m):
        t1, t2 = map(int, input().split())
        graph[t1].append(t2)
        graph[t2].append(t1)
    bfs(graph, a, dist)
    if dist[b] == 0:
        print(-1)
        return
    print(dist[b])

solution()