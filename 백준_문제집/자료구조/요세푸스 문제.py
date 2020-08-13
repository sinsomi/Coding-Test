import sys
n,k=map(int,sys.stdin.readline().split())
nums=[p for p in range(1,n+1)]
ans=[]
temp=k-1
for i in range(n):
    #위치가 리스트를 넘지않으면
    if len(nums) > temp:
        #제거하고 답으로 추가
        ans.append(nums.pop(temp))
        #temp번째 수가 제거 되었고 (k-1)만큼 다음수가 시작이므로
        temp+=k-1
    #위치가 리스트를 넘으면
    elif len(nums) <= temp:
        temp = temp%len(nums)
        # 제거하고 답으로 추가
        ans.append(nums.pop(temp))
        # temp번째 수가 제거 되었고 (k-1)만큼 다음수가 시작이므로
        temp += k-1
print('<',end='')
for i in ans:
    if i==ans[-1]:print(i,end='')
    else: print("%s, "%(i),end='')
print('>',end='')