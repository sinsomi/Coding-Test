nums=[int(input()) for _ in range(9)]
nums.sort()
res=sum(nums)
for i in range(9):
    for j in range(i+1,9):
        if res-nums[i]-nums[j]==100:
            for k in range(9):
                #이부분 잘모르겠음
                if i!=k and j!=k:
                    print(nums[k])