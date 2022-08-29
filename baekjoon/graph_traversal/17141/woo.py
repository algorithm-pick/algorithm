from copy import deepcopy
import sys
from itertools import combinations

def bfs(graph, virus, n):
    for i in virus:
        # print(i)
        graph[i[0]][i[1]] = 3
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 3
    while True:
        temp = []
        zero_before = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] == answer:
                    temp.append((i, j))
                if graph[i][j] == 0 or graph[i][j] == 2:
                    zero_before += 1
        for i in temp:
            for k in range(4):
                nx = i[0] + dx[k]
                ny = i[1] + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                    graph[nx][ny] = graph[i[0]][i[1]] + 1
        # print(graph)
        answer += 1
        zero_after = 0
        for i in graph:
            zero_after += i.count(0)
            zero_after += i.count(2)
        if zero_before == zero_after:
            break
        zero_before = zero_after
    if zero_after == 0:
        return answer - 4
    return 10000

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    answer = 10000
    # graph 입력 받기
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    # virus 정하기
    virus = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                virus.append((i, j))
    virus = list(combinations(virus, m))
    for i in virus:
        temp = bfs(deepcopy(graph), i, n)
        # print(answer)
        # print(temp)
        if temp < answer:
            answer = temp
    if answer == 10000:
        print(-1)
        return
    print(answer)

solution()