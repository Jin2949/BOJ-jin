import sys

N = int(input())
n_lst = list(map(int,sys.stdin.readline().split()))
M = int(input())
m_lst = list(map(int,sys.stdin.readline().split()))

n_lst.sort()

for i in m_lst:
    check = False

    low, high = 0, len(n_lst)-1
    while low <= high:
        mid = (low+high) // 2
        if i > n_lst[mid]:
            low = mid + 1
        elif i < n_lst[mid]:
            high = mid -1
        elif i == n_lst[mid]:
            print(1, end=' ')
            check = True
            break

    if check == False:
        print(0, end= ' ')