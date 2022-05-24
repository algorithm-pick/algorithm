from collections import deque

n=int(input())
m=int(input())

graph=[[]*n for _ in range(n+1)]

for i in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs_recursive(graph, start, visited=[]):
    visited.append(start)
    
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

array=dfs_recursive(graph,1)

print(len(array)-1)
