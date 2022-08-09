N = int(input())
A = list(map(int, input().split()))
M = int(input())
psum = [0]
temp = 0

for i in A:
    temp += i
    psum.append(temp)

for _ in range(M):
    a, b = map(int, input().split())
    print(psum[b]-psum[a-1])
