import math

n = int(input())
arr = list(map(int, input().split()))

# g : 최대 공약수
g = math.gcd(arr[0], arr[1])
if n == 3:
    g = math.gcd(g, arr[2])

result = set()
for i in range(1, int(math.sqrt(g))+1):
    if g % i == 0:
        result.update({i, g // i})
print(*sorted(result), sep='\n')
