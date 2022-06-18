def solution():
    n, l = map(int, input().split())
    leak = list(map(int, input().split()))
    leak.sort()
    current = leak[0] - 0.5 + l
    answer = 1
    for i in leak:
        if i > current:
            current = i - 0.5 + l
            answer += 1
    print(answer)

solution()