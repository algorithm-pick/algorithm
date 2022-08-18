N = int(input())
M = int(input())
heavy = [[] for _ in range(N+1)]
light = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    light[a].append(b)
    heavy[b].append(a)


def search_h(index, visited):
    visited.append(index)

    if len(heavy[index]) > 0:
        for i in heavy[index]:
            if i not in visited:
                search_h(i, visited)
    return visited


def search_l(index, visited):
    visited.append(index)

    if len(light[index]) > 0:
        for i in light[index]:
            if i not in visited:
                search_l(i, visited)
    return visited


for i in range(1, N+1):
    visited = []
    search_h(i, visited)
    search_l(i, visited)
    print(N-len(visited)+1)
