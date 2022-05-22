import sys

input = sys.stdin.readline
n = int(input())
doro = list(map(int, input().split()))
liter = list(map(int, input().split()))

result = doro[0] * liter[0]
price = liter[0]
distance = 0

for i in range(1, n - 1):
    if liter[i] < price:
        result += price * distance
        distance = doro[i]
        price = liter[i]
    else:
        distance += doro[i]
    if i == n - 2:
        result += price * distance

print(result)