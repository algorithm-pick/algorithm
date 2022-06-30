import sys

def solution():
    m, n = map(int, input().split())
    snack = list(map(int, input().split()))
    start = 0
    end = max(snack)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if mid == 0:
            print(0)
            return
        count = 0
        for i in snack:
            count += (i // mid)
        if count >= m:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    print(answer)

solution()