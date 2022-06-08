import sys

time = int(input())

a = 300
b = 60
c = 10

if time % c != 0 :
    print(-1)
else:
    if time // a >= 1:
        print(time//a, end=' ')
        time -= a * (time//a)
    else:
        print(0, end=' ')
    if time // b >= 1:
        print(time//b, end=' ')
        time -= b * (time//b)
    else:
        print(0, end=' ')
    if time // c >= 1:
        print(time//c, end=' ')
        time -= c * (time//c)
    else:
        print(0, end=' ')

