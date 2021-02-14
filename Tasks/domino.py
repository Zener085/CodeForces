def domino(a: int, b: int) -> int:
    if a % 2 == 0 or b % 2 == 0:
        return a * b // 2
    else:
        return (a * b - 1) // 2


m, n = map(int, input().split())

print(domino(m, n))
