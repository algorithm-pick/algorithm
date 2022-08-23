def solution(n, times):
    left = 0
    right = n * max(times)
    while left <= right:
        mid = (left + right) // 2
        temp = 0
        for i in times:
            temp += (mid // i)
        if temp >= n:
            right = mid - 1
        else:
            left = mid + 1
    return right + 1

print(solution(6, [7, 10]))