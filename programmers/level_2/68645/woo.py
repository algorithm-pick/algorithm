def solution(n):
    graph = [[0]*i for i in range(1, n+1)]
    nx = -2
    count = 1
    dx = [1, 0, -1]
    for i in range(n-1, -1, -3):
        nx += 2
        if i == 0:
            ny = graph[nx].index(0)
            graph[nx][ny] = count
            break
        for k in range(2):
            for j in range(i):
                ny = graph[nx].index(0)
                graph[nx][ny] = count
                count += 1
                nx += dx[k]
        for j in range(i):
            ny = len(graph[nx]) - 1 - list(reversed(graph[nx])).index(0)
            graph[nx][ny] = count
            count += 1
            nx -= 1
    return sum(graph, [])

print(solution(6))