import sys

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

i=0
j=N-1
answer = lst[i]+lst[j]
al = i
ar = j

while i<j:
    tot = lst[i]+lst[j]
    if abs(tot)< abs(answer):
        answer = tot
        al = i
        ar = j
        if answer==0:
            break

    if tot < 0:
        i+=1
    else:
        j-=1

print(lst[al], lst[ar])