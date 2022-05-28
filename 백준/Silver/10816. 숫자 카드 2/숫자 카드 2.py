import sys

input = sys.stdin.readline

n = int(input())
n_lst = list(map(int,input().split()))

m = int(input())
m_lst = list(map(int,input().split()))

dict = {}
for i in range(n):
    if n_lst[i] in dict:
        dict[n_lst[i]] +=1
    else:
        dict[n_lst[i]] = 1

for j in range(m):
    rlt = dict.get(m_lst[j])
    if rlt:
        print(rlt, end=' ')
    else:
        print(0, end=' ')