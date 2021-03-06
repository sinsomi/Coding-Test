import sys
n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
visited=[0]*n
ans=[]

def solve(idx,depth):
    if depth==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(n):
        if visited[i]==0 and nums[i]>=idx:
            visited[i]=1
            idx=nums[i]
            ans.append(nums[i])
            solve(idx,depth+1)
            ans.pop()
            visited[i]=0
solve(0,0)