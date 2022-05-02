import sys

N = int(input())
x = 666
cnt = 0
while True:
    if cnt == N:
        x -= 1
        print(x)
        break
    elif '666' in str(x):
        cnt +=1
    x +=1


