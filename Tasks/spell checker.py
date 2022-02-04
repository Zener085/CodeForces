num1 = int(input())
set1 = set(input().split())

num2 = int(input())
set2 = set(input().split())

print(len(set2.difference(set1)))
print(*set2.difference(set1))
