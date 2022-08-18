N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))

limit = score.pop()
final = 0

while score:
    prev = score.pop()
    if prev >= limit:
        down = (prev-limit+1)
        final += down
        prev -= down
    limit = prev
print(final)
