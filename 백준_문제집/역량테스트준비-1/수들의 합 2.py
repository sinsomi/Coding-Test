import sys

n,m=map(int,input().split())
nums=list(map(int,sys.stdin.readline().split()))

def solve():
    left=right=ans=s=0
    while True:
        if s>=m:
            s-=nums[left]
            left+=1
        elif s<m:
            if right==n:
                break
            s+=nums[right]
            right+=1
        if s==m:   #elif가 아닌 if문이므로 while문 돌때마다 확인해줌
            ans+=1
    return ans
print(solve())