n = int(input())

five, two = n // 5, 0

for i in range(five, -1, -1):
    if (n - 5 * i) % 2 == 0:
        print(i + (n - 5 * i) // 2)
        exit(0)
print(-1)