def counting(p: int) -> int:
    if p != 1:
        return counting(p - 1) + p
    else:
        return 1


def t_in_s(a: str, b: str) -> int:
    c = len(b)
    count = 0
    for i in range(len(a) - c):
        if a[i:c] == b:
            count += len(a) - len(a[:i+c])
            continue
    return counting(len(a)) - count


q = int(input())
for x in range(q):
    s = str(input())
    t = str(input())
    print(t_in_s(s, t))
