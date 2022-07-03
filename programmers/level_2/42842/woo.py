import sys

def solution(brown, yellow):
    input = sys.stdin.readline
    answer = []
    w_plus_h = brown // 2 + 2
    width = w_plus_h - 1
    height = 1
    for _ in range(w_plus_h // 2):
        if (width - 2) * (height - 2) == yellow:
            answer.append(width)
            answer.append(height)
            break
        width -= 1
        height += 1
    return answer

print(solution(10, 2))

# 갈색 -> 10
# 10 // 2 = 5
# 5 + 2 = 7
# 6, 1
# 5, 2
# 4, 3