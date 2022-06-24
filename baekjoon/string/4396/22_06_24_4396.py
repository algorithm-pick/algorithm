import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    bomb = []
    for _ in range(n):
        bomb.append(input().strip())
    current = []
    for _ in range(n):
        current.append(input().strip())
    isbomb = False
    for a in range(n):
        for b in range(n):
            if current[a][b] == 'x' and bomb[a][b] == '*':
                isbomb = True
                break
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    for a in range(n):
        temp = ''
        for b in range(n):
            if isbomb and bomb[a][b] == '*':
                temp += '*'
                continue
            if current[a][b] == 'x':
                count = 0
                for i in range(8):
                    nx = a + dx[i]
                    ny = b + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if bomb[nx][ny] == '*':
                        count += 1
                temp += str(count)
            else:
                temp += '.'
        print(temp)
        
solution()