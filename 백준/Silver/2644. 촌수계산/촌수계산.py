import sys

n = int(input())

a, b = map(int,input().split())

m = int(input())

n_bind = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    n_bind[x].append(y)
    n_bind[y].append(x)

def dfs(num, cnt):
    global b
    global rlt
    if num == b:
        rlt = cnt
        return
    if not visited[num]:
        visited[num] = cnt
        for i in n_bind[num]:
            dfs(i, cnt + 1)

visited = [0] * (n+1)

rlt = -1
dfs(a, 1)
if rlt == -1:
    print(-1)
else:
    print(rlt - 1)