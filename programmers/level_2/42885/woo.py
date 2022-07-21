# def solution(people, limit):
#     answer = 0
#     people.sort()
#     while people:
#         answer += 1
#         if len(people) == 1:
#             return answer
#         if (people[0] + people[-1]) <= limit:
#             people.pop(0)
#         people.pop()
#     return answer

def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left <= right:
        answer += 1
        if left == right:
            break
        if (people[left] + people[right]) <= limit:
            left += 1
        right -= 1
    return answer

print(solution([70, 80, 50], 100))