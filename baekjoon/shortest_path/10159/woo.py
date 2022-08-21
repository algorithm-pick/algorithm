import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
    for k in range(n):
        for a in range(n):
            for b in range(n):
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
    for i in range(n):
        answer = 0
        for j in range(n):
            if graph[i][j] == 0 and graph[j][i] == 0:
                answer += 1
        print(answer - 1)

solution()
