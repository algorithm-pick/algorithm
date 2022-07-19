M, N = map(int, input().split())
fiber = []
success = 0

for i in range(M):
    fiber.append(list(map(int, input())))


def bfs(row, col):
    global success
    if row == M-1:
        success = 1
        return

    fiber[row][col] = 1

    if fiber[row+1][col] == 0:
        bfs(row+1, col)
    if col > 0 and fiber[row][col-1] == 0:
        bfs(row, col-1)
    if col < N-1 and fiber[row][col+1] == 0:
        bfs(row, col+1)
    if row > 0 and fiber[row-1][col] == 0:
        bfs(row-1, col)

    return


for i in range(N):
    if fiber[0][i] == 0:
        bfs(0, i)

if success:
    print("YES")
else:
    print("NO")
