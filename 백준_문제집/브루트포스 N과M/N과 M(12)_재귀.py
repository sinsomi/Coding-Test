import sys
n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
ans=[]

def solve(idx,depth):
    if depth==m:
        print(' '.join(map(str,ans)))
        return
    overlap=0
    for i in range(n):
        if nums[i]>=idx and overlap!=nums[i]:
            idx=nums[i]
            overlap=nums[i]
            ans.append(nums[i])
            solve(idx,depth+1)
            ans.pop()
solve(0,0)