def countdown(number: str) -> int:
    res = 0
    number = int(number)
    number = str(number)
    for i in range(1, 10):
        res += number.count(str(i)) * i
        res += number.count(str(i))
        res -= 1 if number[-1] == str(i) else 0
    return res


t = int(input())
for i in range(t):
    n = int(input())
    a = str(input())
    print(countdown(a))
