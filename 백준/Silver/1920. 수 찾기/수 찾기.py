import sys

def find(num):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if N_list[mid] == num:
            return True

        elif N_list[mid] < num:
            left = mid + 1
        elif N_list[mid] > num:
            right = mid - 1

input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int,input().split()))

for i in range(M):
    if find(M_list[i]):
        print(1)
    else:
        print(0)