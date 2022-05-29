a = input()
b = input()

a = list(a)
b = list(b)

same = 0
result = 0

# 1. 받은 값들 역으로 정렬

# 2. 두개가 맞을 때 까지 임의 숫자 하나를 맨 끝으로 보냄
i = 0
while a != b:
    # 인덱스가 같을 경우 패스
    if a[i] == b[i]:
        continue

    # 다를 경우 i번째 인덱스가 b랑 같은걸 찾음
    for j in range(i, len(a)):
        if a[j] == b[i]:
            index = j
            break

    # 해당 인덱스를 맨 앞으로 이동
    temp = a.pop(index)
    # print(a)
    a.insert(0, temp)
    result += 1
    i += 1

print(result)
