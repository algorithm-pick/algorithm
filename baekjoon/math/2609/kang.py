import math

a, b = map(int, input().split())
g = math.gcd(a, b)  # 최대공약수

print(g)
print((a*b)//g)  # 최소공배수
