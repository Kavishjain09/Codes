rows = int(input())
i = 1
while i <= rows:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    print(i, end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print(i)
    i += 1

i = rows - 1
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    print(i, end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print(i)
    i -= 1