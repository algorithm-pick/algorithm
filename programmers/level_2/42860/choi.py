def solution(name):
    name_ascii = []

    for i in name:
        target = ord(i)-ord('A')
        if target > 13:
            target = 26-target
        name_ascii.append(target)

    answer = sum(name_ascii)
    psum = answer
    left, right, cnt = 1, -1, -1

    if psum == 0:
        return 0

    while psum != 0:
        left -= 1
        right += 1
        cnt += 1

        if left < 0:
            left = len(name)-1

        if right > len(name)-1:
            right = 0

        if name_ascii[left] != 0:
            psum -= name_ascii[left]
            name_ascii[left] = 0
            right = left

        elif name_ascii[right] != 0:
            psum -= name_ascii[right]
            name_ascii[right] = 0
            left = right

    answer += cnt

    return answer
