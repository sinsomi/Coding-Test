import sys
n=int(input())
nums=list(map(int,sys.stdin.readline().split()))
ans=[0]*n
for i in range(len(nums)):
    # 비교횟수
    cnt=0
    #맨마지막 인덱스는 비교해줄게 없으므로 종료
    if i==len(nums)-1:
        ans[i]=-1
        break
    #오른쪽 인덱스들에 대해 비교
    for j in range(i+1,len(nums)):
        #오른쪽 애들중에 등장횟수가 더 큰애가 있으면
        if nums.count(nums[i])<nums.count(nums[j]):
            ans[i]+=1
            cnt+=1
        elif nums.count(nums[i])<nums.count(nums[j]):
            cnt+=1
            continue
    if cnt==0:
        ans[i]=-1
print(*ans)