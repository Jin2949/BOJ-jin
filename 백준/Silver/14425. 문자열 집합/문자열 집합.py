import sys

N,M = map(int, sys.stdin.readline().split())

cnt = 0

S = {sys.stdin.readline().strip() for _ in range(N)}

for j in range(M):
    if sys.stdin.readline().strip() in S:
        cnt +=1
print(cnt)