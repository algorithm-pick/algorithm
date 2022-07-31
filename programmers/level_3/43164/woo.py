from collections import defaultdict

def bfs(graph, tickets):
    answer = [['ICN', 'ICN']]
    while tickets:
        current = answer[-1][1]
        if not graph[current]:
            temp = answer.pop()
            tickets.append(temp)
            graph[temp[0]].append(temp[1])
            continue
        temp = graph[current].pop(0)
        answer.append([current, temp])
        tickets.remove([current, temp])
    return answer

def solution(tickets):
    graph = defaultdict(list)
    for i in tickets:
        graph[i[0]].append(i[1])
    for i in graph:
        graph[i].sort()
    answer = []
    for i in bfs(graph, tickets):
        answer.append(i[1])
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))