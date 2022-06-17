# from itertools import permutations

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     com = list(permutations(numbers, len(numbers)))
#     for i in range(len(com)):
#         com[i] = int(''.join(com[i]))
#     return str(max(com))

def solution(numbers):
    answer = ''
    li = []
    for i in numbers:
        temp = str(i) * 4
        li.append([int(temp[:4]), i])
    li.sort(key=lambda x:-x[0])
    for i in li:
        answer += str(i[1])
    if answer[0] == '0':
        return '0'
    return answer

print(solution([3, 30, 34, 5, 9]))