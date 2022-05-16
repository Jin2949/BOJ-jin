import sys

input = sys.stdin.readline

N, K = map(int,input().split())

n_lst = list(map(int,input().split()))

result = []
result.append(sum(n_lst[:K]))

for i in range(N-K):
    result.append(result[i] - n_lst[i] + n_lst[i+K])

print(max(result))