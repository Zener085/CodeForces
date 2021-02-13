n = int(input())
tasks = 0
for i in range(n):
    a, b, c = map(int, input().split())
    tasks += 1 if a + b + c > 1 else 0

print(tasks)
