import sys

t = int(input())

for tc in range(t):
    score_a = 0
    score_b = 0
    for _ in range(9):
        a, b  = map(int,input().split())
        score_a += a
        score_b += b
    if score_a > score_b:
        print('Yonsei')
    elif score_a < score_b:
        print('Korea')
    else:
        print('Draw')
    