def dfs(graph, start, value):
    # 절댓값이면 리턴
    if abs(start) == len(graph):
        if value == 3:
            global result
            result += 1
        return

    value_1 = value + graph[start]
    value_2 = value - graph[start]

    # # 정수한번 음수한번
    dfs(graph, start + 1, value_1)
    dfs(graph, start + 1, value_2)


result = 0
# graph = [4, 1, 2, 1]
graph = [1, 1, 1, 1, 1]
dfs(graph, 0, 0)

print(result)
