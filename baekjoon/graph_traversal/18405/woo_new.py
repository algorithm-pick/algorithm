import sys

# def bfs(graph, v, n):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     for i in range(4):
#         nx = v[0] + dx[i]
#         ny = v[1] + dy[i]
#         if nx < 0 or nx >= n or ny < 0 or ny >= n:
#             continue
#         if graph[nx][ny] == 0:
#             graph[nx][ny] = graph[v[0]][v[1]]

def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    s, x, y = map(int, input().split())
    virus = list(set(sum(graph, [])))
    virus.sort()
    if virus[0] != 0:
        print(graph[x-1][y-1])
        return
    virus.pop(0)
    for _ in range(s):
        for i in virus:
            temp = []
            for a in range(n):
                for b in range(n):
                    if graph[a][b] == i:
                        temp.append((a, b))
            for j in temp:
                # bfs(graph, j, n)
                dx = [-1, 1, 0, 0]
                dy = [0, 0, -1, 1]
                for i in range(4):
                    nx = j[0] + dx[i]
                    ny = j[1] + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[j[0]][j[1]]
            check = list(sum(graph, []))
            if not 0 in check:
                print(graph[x-1][y-1])
                return
    print(graph[x-1][y-1])

solution()