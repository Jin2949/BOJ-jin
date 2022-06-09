import sys
from collections import deque

def bfs():
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()

        if x == b:
            print(location[x])
            break
        for n in (x-1, x+1, x*2):
            if 0<= n <= max and not location[n]:
                location[n] = location[x] + 1
                q.append(n)


max = 10 ** 5
location = [0] * (max + 1)

a, b = map(int,input().split())

bfs()
