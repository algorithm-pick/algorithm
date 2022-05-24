answer = 0

def dfs(graph, visited, v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            global answer
            answer += 1
            dfs(graph, visited, i)

def solution():
    n = int(input())
    m = int(input())
    visited = [False] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        temp1, temp2 = map(int, input().split())
        graph[temp1].append(temp2)
        graph[temp2].append(temp1)
    dfs(graph, visited, 1)
    print(answer)

solution()