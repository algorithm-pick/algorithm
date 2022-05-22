n = int(input())
data = sorted([int(input()) for _ in range(n)], reverse=True)

for i in range(n):
    data[i] = data[i] * (i + 1)

print(max(data))