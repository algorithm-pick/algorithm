from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    for i in clothes:
        clothes_dict[i[1]].append(i[0])
    for i in clothes_dict:
        answer *= (len(clothes_dict[i]) + 1)
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))