def find_palindrome(a: str) -> int:
    x = a[0]
    count = 0
    for i in range(len(a)):
        if x == a[i]:
            if a[:i + 1] == a[:i + 1][::-1]:
                count = i + 1
    return count


t = int(input())
for j in range(t):
    s = str(input())
    print(find_palindrome(s))
