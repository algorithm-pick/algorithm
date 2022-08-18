duck = input()
quack = [0 for _ in range(5)]

for i in duck:
    if i == 'q':
        if quack[-1]:
            quack[-1] -= 1
        quack[0] += 1

    elif quack[0] and i == 'u':
        quack[0] -= 1
        quack[1] += 1

    elif quack[1] and i == 'a':
        quack[1] -= 1
        quack[2] += 1

    elif quack[2] and i == 'c':
        quack[2] -= 1
        quack[3] += 1

    elif quack[3] and i == 'k':
        quack[3] -= 1
        quack[-1] += 1

final = sum(quack)
if (final - quack[-1]) or (not final):
    print(-1)
else:
    print(quack[-1])
