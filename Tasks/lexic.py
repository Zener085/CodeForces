a = str(input()).lower()
b = str(input()).lower()

if a != b:
    for i in range(len(a)):
        if a[i] != b[i]:
            print('1' if ord(a[i]) > ord(b[i]) else '-1')
            break
else:
    print('0')
