import sys

N,S = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))
i = 0
j = 0
total = 0
total = num_list[i]
rlt = 9999999
cnt = 1

while True:
    if total >= S:
        if rlt > cnt:
            rlt = cnt
        total -= num_list[i]
        i +=1
        cnt-=1

    elif total < S:
        j+=1
        cnt+=1
        if j==N:
            break
        total += num_list[j]

if rlt == 9999999:
    print(0)
else:
    print(rlt)