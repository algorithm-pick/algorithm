import sys

def solution():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        sti = []
        sti.append(list(map(int, input().split())))
        sti.append(list(map(int, input().split())))
        answer = 0
        while sum(sum(sti, [])) != 0:
            big = max(sti[0])
            x = 0
            y = sti[0].index(big)
            big2 = max(sti[1])
            x2 = 1
            y2 = sti[1].index(big2)
            if big2 > big:
                big = big2
                x = x2
                y = y2
            answer += big
            sti[x][y] = 0
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 2 or ny < 0 or ny >= n:
                    continue
                sti[nx][ny] = 0
        print(answer)

solution()