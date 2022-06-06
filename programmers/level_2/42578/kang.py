# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    count = {}
    for _, i in clothes:
        if i not in count:
            count[i] = 2
        else:
            count[i] += 1
    answer = 1
    for i in count.values():
        answer *= i
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
