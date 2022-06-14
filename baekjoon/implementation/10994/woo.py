import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    len = (n - 1) * 4 + 1
    star = [[' '] * len for _ in range(len)]
    star[len // 2][len // 2] = '*'
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    nx = 0
    ny = 0
    rotate = len - 1
    for _ in range(n-1):
        for i in range(4):
            for _ in range(rotate):
                star[nx][ny] = '*'
                nx += dx[i]
                ny += dy[i]
        rotate -= 4
        nx += 2
        ny += 2
    for i in star:
        print(''.join(i))

solution()