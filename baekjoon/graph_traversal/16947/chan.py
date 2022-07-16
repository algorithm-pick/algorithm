import copy
import sys
from collections import defaultdict

N = int(input())

graph = [[] * (N + 1) for _ in range(N + 1)]
circle_way = defaultdict(int)

result = [0] * (N + 1)
visited = [False] * (N + 1)


def dfs(v, start, temp_circle):
    # dfs 수행하다가 v 와 start가 한번 더 마주치면 순환선으로 체크
    if (v == start) and v in temp_circle:
        global circle_way
        circle_way = temp_circle
        return

    visited[v] = True
    temp_circle.add(v)

    for subway in graph[v]:
        if not visited[subway] or (len(temp_circle) > 2 and subway == start):
            dfs(subway, start, copy.deepcopy(temp_circle))

    # 순환선은 1개밖에 없기 때문에 False처리
    visited[v] = False

def bfs(v, start)


# Data Initialize
for _ in range(N):
    sub1, sub2 = map(int, sys.stdin.readline().split())
    graph[sub1].append(sub2)
    graph[sub2].append(sub1)

# DFS
for i in range(1, N + 1):
    dfs(i, i, set())


if not circle_way:
    [print(0) for _ in range(N)]
    exit(0)

# BFS로 거리 계산하기
for j in range(1, N + 1):
    if j in circle_way:
        result[j] = 0
        continue

    bfs()
    

    
