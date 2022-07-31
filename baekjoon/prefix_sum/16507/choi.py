r, c, q = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(r)]
p_sum = [[0 for _ in range(c+1)] for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        p_sum[i][j] = p_sum[i-1][j] + p_sum[i][j-1] + \
            picture[i-1][j-1] - p_sum[i-1][j-1]

for i in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    f_sum = p_sum[r2][c2] - p_sum[r1-1][c2] - \
        p_sum[r2][c1-1] + p_sum[r1-1][c1-1]
    avg = f_sum // ((r2-r1+1)*(c2-c1+1))
    print(avg)
