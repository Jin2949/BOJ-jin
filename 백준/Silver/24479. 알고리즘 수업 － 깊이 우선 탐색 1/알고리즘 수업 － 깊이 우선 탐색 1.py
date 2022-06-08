import sys
sys.setrecursionlimit(10**5)

n, m, r = map(int,input().split())
n_bind = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    n_bind[a].append(b)
    n_bind[b].append(a)

for i in range(len(n_bind)):
    n_bind[i].sort()

def dfs(num):
    global cnt
    if not visited[num]:
        visited[num] = cnt
        cnt += 1
        for i in n_bind[num]:
            dfs(i)

cnt = 1

dfs(r)

for j in range(1, n+1):
    print(visited[j])