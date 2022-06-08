import sys

while True:
    n = int(input())
    if n == -1:
        break

    lst = []

    for i in range(1, n//2+1):
        if n % i == 0:
            lst.append(i)

    if n == sum(lst):
        print(n, '=', end=' ')
        for j in lst[:-1]:
            print(j,'+', end=' ')
        print(lst[-1])
    else:
        print(n, 'is NOT perfect.')

