import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 물
def bfs_w(graph, v, r, c):
    x, y = v
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if graph[nx][ny] == '.' or graph[nx][ny] == 'S':
            graph[nx][ny] = '*'

# 고슴도치
def bfs_g(graph, v, r, c):
    x, y = v
    answer = False
    graph[x][y] = '.'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if graph[nx][ny] == '.':
            graph[nx][ny] = 'S'
        if graph[nx][ny] == 'D':
            answer = True
            break
    return answer

def solution():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    graph = []
    for i in range(r):
        graph.append(list(input().strip()))
    count = 0
    while True:
        # 고슴도치
        temp = []
        for a in range(r):
            for b in range(c):
                if graph[a][b] == 'S':
                    temp.append((a, b))
        count += 1
        for i in temp:
            answer = bfs_g(graph, i, r, c)
            if answer == True:
                print(count)
                return

        # 물
        temp = []
        for a in range(r):
            for b in range(c):
                if graph[a][b] == '*':
                    temp.append((a, b))
        for i in temp:
            bfs_w(graph, i, r, c)

        # 고슴도치 남아있는지
        all_blocked = True
        for a in range(r):
            for b in range(c):
                if graph[a][b] == 'S':
                    all_blocked = False
        if all_blocked == True:
            print("KAKTUS")
            return

solution()

# 1

# D.*
# ...
# .S.

# D**
# .S*
# S.S

# D**
# S**
# .S*

# D**
# ***
# .**


# D.*
# ...
# ..S

# D**
# ..*
# .S.

# D**
# .**
# S.*

# D**
# ***
# .**
