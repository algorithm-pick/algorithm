import sys

input = sys.stdin.readline

r, c = map(int, input().split())
data = [input().strip().replace('.', 'D') for _ in range(r)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(r):
    for j in range(c):
        if data[i][j] == 'W':
            for w in range(4):
                ii, jj = i+dx[w], j+dy[w]
                if 0 <= ii < r and 0 <= jj < c and data[ii][jj] == 'S':
                    print(0)  # 늑대가 접근 가능
                    exit(0)   # 더 볼것도 없이 바로 종료

print(1)
print(*data, sep='\n')
