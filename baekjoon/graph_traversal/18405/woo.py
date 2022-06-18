import sys

def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    s, x, y = map(int, input().split())
    virus = list(set(sum(graph, [])))
    virus.sort()
    if virus[0] == 0:
        virus.pop(0)
    for _ in range(s):
        for i in virus:
            find = []
            for a in range(n):
                for b in range(n):
                    if graph[a][b] == i:
                        find.append((a, b))
            for r in find:
                dx = [-1, 1, 0, 0]
                dy = [0, 0, -1, 1]
                for p in range(4):
                    nx = r[0] + dx[p]
                    ny = r[1] + dy[p]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = i
            temp = list(sum(graph, []))
            if not 0 in temp:
                print(graph[x-1][y-1])
                return
    print(graph[x-1][y-1])

solution()