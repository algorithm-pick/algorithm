import sys

def solution():
    answer = 0
    input = sys.stdin.readline
    n = int(input())
    levels = [int(input()) for _ in range(n)]
    for i in range(n-2, -1, -1):
        if levels[i] >= levels[i+1]:
            answer += (levels[i] - levels[i+1] + 1)
            levels[i] = levels[i+1] - 1
    print(answer)

solution()