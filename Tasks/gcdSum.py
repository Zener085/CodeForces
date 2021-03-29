from math import gcd


def gcdsum(a: int) -> int:
    b = 0
    c = a
    while c > 0:
        b += c % 10
        c = c // 10
    return gcd(a, b)


def find_gcd(x: int) -> int:
    while gcdsum(x) <= 1:
        x += 1
    return x


t = int(input())
for i in range(t):
    n = int(input())
    print(find_gcd(n))
