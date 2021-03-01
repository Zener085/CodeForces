def reverse(a: int, b: int) -> int:
    result = 0
    for i in range(a):
        result += (i+1) * b

    return result


k, n, w = map(int, input().split())
credit = reverse(n, k) - n
print(credit)
