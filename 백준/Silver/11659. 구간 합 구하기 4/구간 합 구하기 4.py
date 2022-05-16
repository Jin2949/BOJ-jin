import sys

input = sys.stdin.readline

N, M = map(int,input().split())

n_lst = list(map(int,input().split()))

for i in range(N-1):
    n_lst[i+1] += n_lst[i]
n_lst = [0] + n_lst

for _ in range(M):
    a,b =map(int,input().split())
    print(n_lst[b]-n_lst[a-1])

