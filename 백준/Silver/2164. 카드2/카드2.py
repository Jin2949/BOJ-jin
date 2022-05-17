import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

q= deque()

for i in range(1,N+1):
    q.append(i)

while True:
    if len(q)==1:
        print(q[0])
        break
    q.popleft()
    q.append(q[0])
    q.popleft()
