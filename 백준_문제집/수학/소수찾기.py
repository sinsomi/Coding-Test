import sys

n=int(input())
nums=list(map(int,sys.stdin.readline().split()))
res=0
count=0

for i in nums:
    #각각 수 비교해줄때마다 count는 초기화
    count=0
    #1부터 i+1까지(즉 1부터 자기자신까지 나눔)
    for j in range(1,i+1):
        #나누어 떨어지면 count 증가
        if i%j==0:
            count+=1
    #count가 2이면 소수
    if count==2:
        res+=1
print(res)
