import sys
n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
ans=[]

def solve(depth):
    if depth==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(n):
        ans.append(nums[i])
        solve(depth+1)
        ans.pop()
solve(0)