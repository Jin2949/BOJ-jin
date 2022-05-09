import sys

N = int(input())

for i in range(1,N+1):
    nums = list(map(int,str(i)))
    total = i + sum(nums)
    if total == N:
        print(i)
        break
    elif N == i:
        print(0)

