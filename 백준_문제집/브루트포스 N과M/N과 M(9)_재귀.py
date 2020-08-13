import sys
n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
visited=[0]*n
ans=[]
real_ans=[]
def solve(depth):
    if depth==m:
        print(' '.join(map(str, ans)))
        return
    #overlap변수를 선언
    #초기값은 0, 그다음부턴 비교해주는 값(nums[i])을 대입한후
    #overlap이 nums[i]와 같은지 비교
    overlap=0
    for i in range(n):
        if visited[i]==0 and overlap!=nums[i]:
            visited[i]=1
            overlap=nums[i]
            ans.append(nums[i])
            solve(depth+1)
            ans.pop()
            visited[i]=0
solve(0)