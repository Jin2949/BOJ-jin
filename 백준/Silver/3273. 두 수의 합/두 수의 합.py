import sys

N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())

numbers.sort()

i = 0
j = N-1
cnt = 0
while i<j:
    if numbers[i]+numbers[j]==x:
        cnt+=1
        i+=1
        j-=1
    elif numbers[i]+numbers[j]<x:
        i+=1
    elif numbers[i]+numbers[j]>x:
        j-=1
        
print(cnt)

