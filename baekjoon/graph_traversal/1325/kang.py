import sys
from collections import deque


def bfs(graph, start):
    visited, queue = [False]*(n+1),  deque([start])
    visited[start] = True
    count = 1
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[b].append(a)

result = []
max_count = -1
for i in range(1, n + 1):
    temp = bfs(arr, i)
    if temp > max_count:
        result = [i]
        max_count = temp
    elif temp == max_count:
        result.append(i)

print(*result)
