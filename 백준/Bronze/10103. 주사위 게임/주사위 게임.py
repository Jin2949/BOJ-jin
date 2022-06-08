import sys

n = int(input())

score_1 = 100
score_2 = 100

for _ in range(n):
    a, b = map(int,input().split())
    if a > b:
        score_2 -= a
    elif a < b:
        score_1 -= b
        
print(score_1)
print(score_2)