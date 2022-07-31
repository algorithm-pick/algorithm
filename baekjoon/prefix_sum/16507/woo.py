import sys

def solution():
    input = sys.stdin.readline
    r, c, q = map(int, input().split())
    graph = [[0] * (c+1)]
    for _ in range(r):
        temp = [0] + list(map(int, input().split()))
        graph.append(temp)
    for a in range(1, r+1):
        for b in range(1, c+1):
            graph[a][b] += (graph[a-1][b] + graph[a][b-1] - graph[a-1][b-1])
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        sum = graph[r2][c2] - graph[r2][c1-1] - graph[r1-1][c2] + graph[r1-1][c1-1]
        count = (r2-r1+1) * (c2-c1+1)
        print(sum // count)

solution()

# 4 1 3 4 9 5
# 1 2 8 7 5 5
# 8 1 2 5 3 2
# 1 5 3 4 2 5
# 5 2 1 2 3 5

# 0 0 0 0 0 0 0
# 0 4 1 3 4 9 5
# 0 1 2 8 7 5 5
# 0 8 1 2 5 3 2
# 0 1 5 3 4 2 5
# 0 5 2 1 2 3 5

# [0, 0, 0, 0, 0, 0, 0]
# [0, 4, 5, 8, 12, 21, 26]
# [0, 5, 8, 19, 30, 44, 54]
# [0, 13, 17, 30, 46, 63, 75]
# [0, 14, 23, 39, 59, 78, 95]
# [0, 19, 30, 47, 69, 91, 113]