def solution(progresses, speeds):
    answer = []
    progresses.append(0)
    speeds.append(1)
    current, temp = divmod(100 - progresses[0], speeds[0])
    if temp != 0:
        current += 1
    count = 1
    for i in range(1, len(progresses)):
        a, b = divmod(100 - progresses[i], speeds[i])
        if b != 0:
            a += 1
        if a > current:
            answer.append(count)
            current = a
            count = 1
        else:
            count += 1
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))