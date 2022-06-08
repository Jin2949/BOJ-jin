import sys

t = int(input())

for tc in range(t):
    N = int(input())
    school, alchoal = '', 0
    for _ in range(N):
        a, b = input().split()
        if int(b) > int(alchoal):
            school, alchoal = a, b
    print(school)