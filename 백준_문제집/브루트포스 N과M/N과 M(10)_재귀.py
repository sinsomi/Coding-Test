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
    overlap=0
    for i in range(n):
        if overlap != nums[i] and nums[i]>=idx and visited[i]==0:
            visited[i]=1
            idx=nums[i]
            overlap=nums[i]
            ans.append(nums[i])
            solve(idx,depth+1)
            ans.pop()
            visited[i]=0
solve(0,0)