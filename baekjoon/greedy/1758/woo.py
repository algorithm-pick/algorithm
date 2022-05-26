def solution():
    n = int(input())
    tips = [int(input()) for _ in range(n)]
    tips.sort(reverse=True)
    answer = 0
    for i in range(n):
        if tips[i] - i <= 0:
            break
        answer += (tips[i] - i)
    print(answer)

solution()