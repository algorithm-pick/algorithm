from collections import deque

def solution(priorities, location):
    wait = deque([])
    answer = []
    for i in range(len(priorities)):
        wait.append([priorities[i], i])
    while wait:
        temp = wait.popleft()
        if not wait:
            answer.append(temp[1])
            break
        temp2 = max(wait, key=lambda x: x[0])
        if temp[0] < temp2[0]:
            wait.append(temp)
        else:
            answer.append(temp[1])
    return answer.index(location) + 1

print(solution([2, 1, 3, 2], 2))