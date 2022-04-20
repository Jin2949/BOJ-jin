import sys
import heapq

N = int(sys.stdin.readline())

queue = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x==0:
        if queue:
            print((-1)*heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, -x)
