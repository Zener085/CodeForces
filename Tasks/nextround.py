n, k = map(int, input().split())
a = list(map(int, input().split()))

print(sum(0 < x >= a[k - 1] for x in a) if sum(x > 0 for x in a) > 0 else 0)
