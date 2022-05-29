#달팽이
def solution():
    n = int(input())
    n_find = int(input())
    li = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    start = n // 2
    nx = start
    ny = start
    count = 1
    li[nx][ny] = count
    for i in range(2, n, 2):
        nx -= 1
        ny -= 1
        for j in range(4):
            for _ in range(i):
                count += 1
                nx += dx[j]
                ny += dy[j]
                li[nx][ny] = count
            # print(li)
    answer = []
    for i in range(n):
        print(*li[i])
        if n_find in li[i]:
            answer.append(i+1)
            answer.append(li[i].index(n_find)+1)
    print(*answer)

solution()