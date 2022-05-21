def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        apply = [list((map(int, input().split()))) for _ in range(n)]
        apply.sort(key=lambda x: x[0])
        answer = 1
        temp = apply[0][1]
        for i in range(1, n):
            if apply[i][1] < temp:
                temp = apply[i][1]
                answer += 1
        print(answer)

solution()

# 2
# 5
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5
# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1