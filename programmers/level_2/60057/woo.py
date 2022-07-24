def solution(s):
    s_len = len(s)
    answer = 1000
    if s_len == 1:
        return 1
    for i in range(1, s_len//2+1):
        s_copy = s[:]
        current = s[:i]
        count = 1
        s_copy = s_copy[i:]
        temp = ''
        while True:
            if len(s_copy) < i:
                if count == 1:
                    temp += current
                else:
                    temp += str(count)
                    temp += current
                temp += s_copy
                break
            pop = s_copy[:i]
            s_copy = s_copy[i:]
            if pop == current:
                count += 1
                continue
            else:
                if count == 1:
                    temp += current
                else:
                    temp += str(count)
                    temp += current
                current = pop
                count = 1
        if len(temp) < answer:
            answer = len(temp)
    return answer

print(solution("a"))
