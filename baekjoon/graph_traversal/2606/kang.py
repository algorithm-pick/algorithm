from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def bfs(graph, start):
    visited, queue = list(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += graph[node]
    return visited


def dfs(graph, start):
    visited, stack = list(), deque([start])
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += graph[node]
    return visited


n = int(input())    # 컴퓨터 수
arr = defaultdict(list)

for _ in range(int(input())):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

print(len(bfs(arr, 1))-1)
# print(len(dfs(arr, 1))-1)
