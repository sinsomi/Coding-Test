import sys
n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
ans=[]

def solve(idx,depth):
    if depth==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(n):
        if nums[i]>=idx:
            idx=nums[i]
            ans.append(nums[i])
            solve(idx,depth+1)
            ans.pop()
solve(0,0)