import sys

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    left, right = 1, min(a) * m
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        balloon = 0
        for t in a:
            balloon += mid // t
            if balloon >= m:
                break
        if balloon >= m:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)

solution()