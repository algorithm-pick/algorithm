from collections import deque

def bfs(graph, v):
    answer = 1
    queue = deque([v])
    visited = [False] * (len(graph))
    visited[v] = True
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                answer += 1
    return answer

def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    answer = [0] * (n+1)
    for _ in range(m):
        temp1, temp2 = map(int, input().split())
        graph[temp2].append(temp1)
    for i in range(1, n+1):
        answer[i] = bfs(graph, i)
    for i in range(1, n+1):
        if answer[i] == max(answer):
            print(i, end=' ')

solution()