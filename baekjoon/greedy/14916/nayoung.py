def solution():
    money = int(input())
    answer = 0
    if money % 5 == 0:
        print(money // 5)
        return
    while(True):
        money = money - 2
        answer += 1
        if money % 5 == 0:
            answer += money // 5
            break
        if money == 0:
            break
        if money < 0:
            answer = -1
            break
    print(answer)

solution()