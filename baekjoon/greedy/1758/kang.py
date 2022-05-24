import sys

input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)
answer = 0
for i in range(n):
    if arr[i] - i > 0:
        answer += arr[i] - i
print(answer)
