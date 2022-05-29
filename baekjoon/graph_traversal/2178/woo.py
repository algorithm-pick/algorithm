dx = [-1, 1, 0]
dy = [0, 0, 1]
answer = []

def dfs(graph, visited, x, y, sum):
    visited[x][y] = True
    sum += 1
    if x == len(graph) - 2 and y == len(graph[0]) - 2:
        answer.append(sum)
        return
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if not visited[nx][ny] and graph[nx][ny] == '1':
            dfs(graph, visited, nx, ny, sum)

def solution():
    n, m = map(int, input().split())
    graph = [['0']*(m+2) for _ in range(n+2)]
    for i in range(1, n+1):
        graph[i][1:m+1] = list(input())
    visited = [[False]*(m+2) for _ in range(n+2)]
    dfs(graph, visited, 1, 1, 0)
    print(min(answer))

solution()