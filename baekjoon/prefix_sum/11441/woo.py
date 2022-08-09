import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    num = list(map(int, input().split()))
    for i in range(1, n):
        num[i] += num[i-1]
    m = int(input())
    for _ in range(m):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        if i == 0:
            print(num[j])
            continue
        print(num[j] - num[i-1])

solution()