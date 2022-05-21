def solution():
    n, m = map(int, input().split())
    answer = 0
    money = [int(input()) for _ in range(n)]
    money.reverse()
    for i in money:
        temp = m // i
        m -= (i * temp)
        answer += temp
    print(answer)

solution()