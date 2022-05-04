import sys

n, m, k = map(int,input().split())
rlt = 0
for i in range(k+1):
    women = n-i
    men = m-(k-i)
    rlt = max(min(women//2, men), rlt)
print(rlt)
