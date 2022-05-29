# https://programmers.co.kr/learn/courses/30/lessons/68645
def solution1(n):
    answer = [[0] * i for i in range(1, n + 1)]
    max_num = (n * (n + 1)) // 2  # 삼각 달팽이에 채워질 마지막 수
    num = 1  # 시작 수
    directions = [(1, 0), (0, 1), (-1, -1)]  # 아래, 오른쪽, 대각선(오른쪽 아래-> 왼쪽 위)
    x, y = -2, -1  # 초기화 좌표
    while n > 0:
        x += 2
        y += 1
        for xx, yy in directions:
            for i in range(n - 1):
                answer[x][y] = num  # 숫자 채우기
                x += xx
                y += yy
                num += 1
        n -= 3
    if num == max_num:  # 딱 가운데 하나만 남는 경우
        answer[x][y] = max_num
    return sum(answer, [])


def solution2(n):
    answer = [[0] * i for i in range(1, n + 1)]
    x, y = -1, 0
    num = 1  # 시작 수
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  # 하
                x += 1
            elif i % 3 == 1:  # 우
                y += 1
            else:  # 상
                x -= 1
                y -= 1
            answer[x][y] = num  # 숫자 채우기
            num += 1
    return sum(answer, [])
