from collections import deque


N, M = map(int,input().split()) #N세로, M가로
r,c,d = map(int,input().split())
# d :0 북 , 1동 , 2남, 3서
#북->서, 서->남, 남->동, 동->북
matrix=[list(map(int,input().split())) for _ in range(N)]

dr,dc = [-1,0,1,0],[0,1,0,-1]   #북동남서
q = deque()
q.append((r,c))
cnt = 0
while q:
    r,c = q.popleft()
    if matrix[r][c]==0:
        cnt +=1
        matrix[r][c]=2



    check = 0
    for _ in range(4):
        check +=1
        d = (d+3)%4
        rr, cc = r+dr[d], c+dc[d]
        if matrix[rr][cc]==0:
            q.append((rr,cc))
            break
    if q:
        pass
    else:
        if check == 4:
            d = (d + 2) % 4
            rrr, ccc = r + dr[d], c + dc[d]
            if matrix[rrr][ccc]==1:
                #아예 멈춰
                break
            else:
                q.append((rrr,ccc))
                d = (d+2)%4

print(cnt)



