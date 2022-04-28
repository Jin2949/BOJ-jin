import sys
from collections import deque
def dfs(n):
    print(n, end=' ')
    visited[n] = 1
    for i in matrix[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    visited[n]=1
    q = deque()
    q.append(V)
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for m in matrix[x]:
            if not visited[m]:
                q.append(m)
                visited[m] =1


N, M, V = map(int,input().split())
matrix = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    i, j = map(int,input().split())
    matrix[i].append(j)
    matrix[j].append(i)

for i in range(1,N+1):
    matrix[i].sort()

dfs(V)
print()
visited = [0] * (N+1)
bfs(V)