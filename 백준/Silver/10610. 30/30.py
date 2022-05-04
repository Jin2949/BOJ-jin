import sys

n_lst = list(map(int,input()))

n_lst.sort(reverse=True)
rlt = ''
if n_lst[-1] !=0 or sum(n_lst[:-1])%3 !=0:
    print(-1)
else:
    for i in n_lst:
        rlt += str(i)
    print(int(rlt))