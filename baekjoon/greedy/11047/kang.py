import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
result = 0

for coin in coins[::-1]:
    temp, k = divmod(k, coin)
    result += temp
    if k == 0:
        break

print(result)