def solution():
    n, m = map(int, input().split())
    farm = [['D']*(m+2) for _ in range(n+2)]
    for i in range(1, n+1):
        farm[i][1:m+1] = list(input().replace('.', 'D'))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if farm[i][j] == 'W':
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if farm[nx][ny] == 'S':
                        print(0)
                        return
    print(1)
    for i in range(1, n+1):
        print(''.join(farm[i][1:m+1]))

solution()