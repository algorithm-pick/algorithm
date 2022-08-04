import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    graph = []
    visited = [[0] * n for _ in range(n)]
    answer = -1
    for _ in range(n):
        graph.append(list(input().strip()))
    for k in range(n):
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                if (graph[a][k] == 'Y' and graph[k][b] == 'Y') or graph[a][b] == 'Y':
                    visited[a][b] = 1
    for i in visited:
        if sum(i) > answer:
            answer = sum(i)
    print(answer)

solution()