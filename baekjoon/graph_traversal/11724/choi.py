import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]


def dfs(g, s, check):
    check[s] = 1

    for i in g[s]:
        if not check[i]:
            dfs(g, i, check)


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(N):
    if not check[i]:
        cnt += 1
        dfs(graph, i, check)
cnt -= 1
