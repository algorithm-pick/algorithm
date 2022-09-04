import itertools

def solution(user_id, banned_id):
    answer = []
    per_list = list(itertools.permutations(user_id, len(banned_id)))
    for i in per_list:
        diff1 = True
        for j in range(len(banned_id)):
            if len(i[j]) != len(banned_id[j]):
                diff1 = False
                break
            diff2 = True
            for k in range(len(i[j])):
                if banned_id[j][k] == "*":
                    continue
                if i[j][k] != banned_id[j][k]:
                    diff2 = False
                    break
            if not diff2:
                diff1 = False
                break
        if diff1:
            if set(i) not in answer:
                answer.append(set(i))
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))