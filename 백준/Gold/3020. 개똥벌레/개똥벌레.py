import sys

n, h = map(int, input().split())

top = [0] * (h+1)
bottom = [0] * (h+1)

for i in range(n):
    if i%2:
        top[int(input())] += 1
    else:
        bottom[int(input())] += 1

for j in range(h,0,-1):
    top[j-1] = top[j] + top[j-1]
    bottom[j-1] = bottom[j] + bottom[j-1]

cnt = n
range_cnt = 0

for k in range(1, h+1):
    if cnt > bottom[k] + top[h-k+1]:
        cnt = bottom[k] + top[h-k+1]
        range_cnt = 1
    elif cnt == bottom[k] + top[h-k+1]:
        range_cnt += 1
print(cnt, range_cnt)