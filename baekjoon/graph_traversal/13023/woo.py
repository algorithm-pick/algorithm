from collections import defaultdict
import copy

answer = []

def bfs(graph, visited, v, sum):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            temp = copy.deepcopy(visited)
            bfs(graph, temp, i, sum + 1)
    answer.append(sum)

def solution():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(n):
        visited = defaultdict(bool)
        bfs(graph, visited, i, 0)
        if max(answer) >= 4:
            print(1)
            return
    print(0)
    return

solution()