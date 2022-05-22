import sys

input = sys.stdin.readline
n = int(input())
data = sorted(map(int, input().split()))

for i in range(1, n):
    data[i] += data[i - 1]
print(sum(data))