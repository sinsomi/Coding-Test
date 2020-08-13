import sys
n,m=map(int,sys.stdin.readline().split())
ans=[]
idx=0

def solve(idx,depth):
    if depth==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(1,n+1):
        #i>=idx 요부분이 쪼금 헷갈림!!
        if i>=idx:
            idx=i
            ans.append(i)
            solve(idx,depth+1)
            ans.pop()
solve(0,0)