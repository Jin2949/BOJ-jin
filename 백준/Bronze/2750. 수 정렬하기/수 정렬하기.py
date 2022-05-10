import sys

N = int(input())
lst = []
for _ in range(N):
    i = int(input())
    lst.append(i)
lst.sort()
for i in lst:
    print(i)