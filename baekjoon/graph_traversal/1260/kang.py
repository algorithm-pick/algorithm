from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def dfs(graph, start):
    visited, stack = list(), deque([start])
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += sorted(graph[node], reverse=True)
    return visited


def bfs(graph, start):
    visited, queue = list(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += sorted(graph[node])
    return visited


n, m, v = map(int, input().split())
arr = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

print(*dfs(arr, v))
print(*bfs(arr, v))
