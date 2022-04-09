from collections import deque

N, M = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dr,dc = [-1,1,0,0],[0,0,-1,1]
rlt = 0
q= deque()

def bfs():
    global rlt
    new_matrix = [mat[:] for mat in matrix[:]]
    for i in range(N):
        for j in range(M):
            if new_matrix[i][j]==2:
                q.append((i,j))

    while q:
        r, c = q.popleft()
        for k in range(4):
            rr,cc = r+dr[k], c+dc[k]
            if 0<=rr<N and 0<=cc<M and not new_matrix[rr][cc]:
                new_matrix[rr][cc]=2
                q.append((rr,cc))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_matrix[i][j]==0:

                cnt+=1
    rlt = max(rlt,cnt)
    return


def wall(w):
    if w==3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if not matrix[i][j]:
                    matrix[i][j]=1
                    wall(w+1)
                    matrix[i][j]=0
rlt = 0
wall(0)
print(rlt)