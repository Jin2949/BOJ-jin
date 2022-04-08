import sys
from collections import deque

N = int(input())
K = int(input())
matrix = [[0]*N for _ in range(N)]

for i in range(K):
    a,b = map(int,input().split())
    matrix[a-1][b-1] = 1

dir = int(input())
direction = deque()
for j in range(dir):
    x,d = input().split()
    x = int(x)
    direction.append((x,d))


dr,dc = [0,1,0,-1],[1,0,-1,0] #우하좌상
#오른쪽 :+1%4 왼쪽: +3%4
t = 0
r,c = 0,0 #뱀 처음위치
visited=deque()
d = 0

while True:
    t+=1
    matrix[r][c] = 9
    rr,cc = r+dr[d], c+dc[d]

    if not 0<=rr<N or not 0<=cc<N or matrix[rr][cc]==9:

        break

    visited.append((r,c))

    if matrix[rr][cc]==0:
        x,y = visited.popleft()
        matrix[x][y] = 0

    matrix[rr][cc] = 9

    if direction and t == direction[0][0]:

        t, dd = direction.popleft()
        if dd == 'D':
            d= (d+1)%4
        else:
            d = (d+3)%4
    r,c = rr, cc

print(t)