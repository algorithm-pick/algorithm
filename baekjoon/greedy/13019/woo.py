#A를B로
def solution():
    a = input()
    b = input()
    n = len(a)
    if set(list(a)) - set(list(b)) != set():
        print(-1)
        return
    answer = 0
    end = n
    for i in range(n-1, 0, -1):
        if a[i:n] != b[i:n]:
            break
        end -= 1
    for i in range(0, end):
        if a[:end].rfind(b[i:end]) != -1:
            answer = i
            break
    print(answer)

solution()