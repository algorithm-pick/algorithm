def solution():
    n = int(input())
    loop = [int(input()) for _ in range(n)]
    loop.sort(reverse=True)
    answer = loop[0]
    for i in range(1, n):
        if answer < loop[i] * (i+1):
            answer = loop[i] * (i+1)
    print(answer)

solution()