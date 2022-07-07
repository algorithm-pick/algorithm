def solution(s):
    s = s[1:len(s)-1]
    arr = s.split('},')
    for i in range(len(arr)):
        arr[i] = arr[i].replace('{', '')
        arr[i] = arr[i].replace('}', '')
        arr[i] = arr[i].split(',')
    arr.sort(key=len)
    answer = [int(arr[0][0])]
    for i in range(1, len(arr)):
        temp = list(set(arr[i]) - set(arr[i - 1]))
        answer.append(int(temp[0]))
    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))