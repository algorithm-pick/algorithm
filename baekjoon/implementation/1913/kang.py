n, find_pos = int(input()), int(input())
arr = [[0]*n for _ in range(n)]  # 출력할 표
arr[n//2][n//2] = 1
result_pos = (n//2+1, n//2+1)   # 1일때 위치로 초기화

number = n*n
x, y = -1, -1   # 현재 위치
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 방향
while n > 0:
    x += 1
    y += 1
    for xx, yy in directions:
        for i in range(n-1):
            arr[x][y] = number
            if number == find_pos:  # 현재 수가 위치를 찾는 수라면
                result_pos = (x+1, y+1)
            number -= 1
            x += xx
            y += yy
    n -= 2

for i in arr:   # 표 출력
    print(*i)
print(*result_pos)  # 찾는 수 위치 출력
