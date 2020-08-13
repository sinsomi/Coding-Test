import sys
n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
visited=[0]*n
ans=[]

def solve(depth,n,m):
    if depth==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            ans.append(nums[i])
            solve(depth+1,n,m)
            ans.pop()
            visited[i] = 0
solve(0,n,m)