def abbreviation(s: str) -> str:
    return s[0] + str(len(s) - 2) + s[-1]


n = int(input())
for i in range(n):
    t = str(input())
    print(abbreviation(t) if len(t) > 10 else t)
