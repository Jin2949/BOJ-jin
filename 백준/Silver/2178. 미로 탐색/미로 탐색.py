from collections import deque

N, M = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
r,c = (0,0)
q = deque()
q.append((r,c))
dr,dc = [-1,1,0,0],[0,0,-1,1]
visited[r][c]=1
cnt = 0
rlt = 0
while q:
    r,c = q.popleft()
    for i in range(4):
        rr,cc = r+dr[i], c+dc[i]
        if 0<=rr<N and 0<=cc<M and matrix[rr][cc] and not visited[rr][cc]:
            visited[rr][cc] = visited[r][c]+1
            q.append((rr,cc))

print(visited[N-1][M-1])
