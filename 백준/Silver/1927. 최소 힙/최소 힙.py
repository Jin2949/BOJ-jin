import sys
import heapq

N = int(sys.stdin.readline())

q = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x==0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,x)




