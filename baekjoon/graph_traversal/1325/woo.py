#시간초과

from collections import defaultdict, deque

def bfs(graph, visited, v):
    answer = 1
    queue = deque([v])
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
    graph = defaultdict(list)
    answer = [0] * (n+1)
    for _ in range(m):
        temp1, temp2 = map(int, input().split())
        graph[temp2].append(temp1)
    print(graph)
    for i in range(1, n+1):
        visited = defaultdict(bool)
        answer[i] = bfs(graph, visited, i)
    for i in range(1, n+1):
        if answer[i] == max(answer):
            print(i, end=' ')

solution()