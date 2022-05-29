import math

def solution():
    n, m = map(int, input().split())
    print(math.gcd(n, m))
    print(math.lcm(n, m))

solution()