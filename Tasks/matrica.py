for i in range(5):
    a = list(map(int, input().split()))
    if 1 in a:
        if i == 2:
            if a.index(1) == 2:
                print(0)
            elif a.index(1) in (1, 3):
                print(1)
            else:
                print(2)
        elif i in (1, 3):
            if a.index(1) == 2:
                print(1)
            elif a.index(1) in (1, 3):
                print(2)
            else:
                print(3)
        else:
            if a.index(1) == 2:
                print(2)
            elif a.index(1) in (1, 3):
                print(3)
            else:
                print(4)