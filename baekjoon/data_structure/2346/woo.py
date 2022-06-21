import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    n = int(input())
    balloon = deque(list(map(int, input().split())))
    for i in range(1, n+1):
        balloon[i-1] = [balloon[i-1], i]
    for _ in range(n):
        temp = balloon.popleft()
        print(temp[1], end=' ')
        if temp[0] < 0:
            balloon.rotate(temp[0] * -1)
        else:
            balloon.rotate((temp[0] - 1) * -1)

solution()