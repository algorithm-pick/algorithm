from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def bfs(graph, start, result):
    visited, queue = defaultdict(bool), deque([start])
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                result[i] = node
                queue.append(i)


n = int(input())
arr, result = defaultdict(list), defaultdict(int)

for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

bfs(arr, 1, result)

for i in range(2, n+1):
    print(result[i])
