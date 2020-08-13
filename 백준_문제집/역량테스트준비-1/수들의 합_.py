import sys

n,m=map(int,input().split())
nums=list(map(int,sys.stdin.readline().split()))
sum_nums=[0]*(n+1)

#0-n까지의 합
for i in range(1,n+1):
    sum_nums[i]=sum_nums[i-1]+nums[i-1]

ans=0
#j까지의 합 - i까지의 합
for i in range(n):
    for j in range(i+1,n+1):
        if sum_nums[j]<m:  #sum_A[j]가 너무 작아서 해당 수를 만들 수 없는 경우
            pass
        elif sum_nums[j]-sum_nums[i]>m:  #sum_A[j]가 너무 커서 벗어난 경우
            break
        elif sum_nums[j]-sum_nums[i]==m:
            ans+=1
            break
print(ans)