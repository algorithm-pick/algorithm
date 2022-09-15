from collections import deque

def bfs(graph, n, m):
    queue = deque([(0, 0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        temp = queue.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[temp[0]][temp[1]] + 1
                queue.append((nx, ny))

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    bfs(maps, n, m)
    if maps[n-1][m-1] <= 1:
        return -1
    return maps[n-1][m-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))