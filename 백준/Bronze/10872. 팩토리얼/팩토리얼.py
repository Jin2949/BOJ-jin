def fact(N, rlt):
    if N==0:
        print(rlt)
        return
    rlt *= N
    fact(N-1,rlt)


N = int(input())
fact(N,1)