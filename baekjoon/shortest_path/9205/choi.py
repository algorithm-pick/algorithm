t = int(input())

for _ in range(t):
    n = int(input())
    building = []
    visit = [False for _ in range(n+2)]

    def check(current):
        visit[current] = True

        for i, v in enumerate(visit):
            if not v:
                x = abs(building[current][0] - building[i][0])
                y = abs(building[current][1] - building[i][1])
                if x+y <= 20*50:
                    check(i)
        return

    for _ in range(n+2):
        temp = list(map(int, input().split()))
        building.append(temp)

    check(0)

    if visit[-1]:
        print("happy")
    else:
        print("sad")
