import sys

n = int(input()) #컴퓨터수
m = int(input()) #컴퓨터 쌍수

bind_n = [[] for _ in range (n+1) ]
visited = [0] * (n+1)
visited[0] = 1

for _ in range(m):
    x, y = map(int,input().split())
    bind_n[x].append(y)
    bind_n[y].append(x)

cnt = 0
visited = [0] * (n+1)

def dfs(start):
    global cnt
    visited[start] = 1
    for i in bind_n[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)