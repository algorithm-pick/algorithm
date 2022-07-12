from collections import defaultdict, deque

def bfs(graph, visited, v, n):
    visited[v] = True
    queue = deque([v])
    while queue:
        temp = queue.popleft()
        for i in range(n):
            if not visited[i] and graph[temp][i] == 1:
                queue.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    visited = defaultdict(bool)
    for i in range(n):
        if not visited[i]:
            bfs(computers, visited, i, n)
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))