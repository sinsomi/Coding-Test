import math

n=int(input())
nums = []

#prime()함수 다시보기
def prime():
    c = [False]*(n+1)
    for i in range(2, n+1):
        if i*i > n:
            break
        #아직 지우지 않은 숫자중에서
        if not c[i]:
            #i의 배수를 전부 제거함
            for j in range(i*i, n+1, i):
                c[j] = True
    #소수인 수들만 nums에 추가
    for i in range(2, n+1):
        if not c[i]:
            nums.append(i)

def solve():
    left=right=ans=s=0
    k=len(nums)
    while True:
        if s>=n:
            s-=nums[left]
            left+=1
        else:
            if right==k:
                break
            s+=nums[right]
            right+=1
        if s==n:
            ans+=1
    print(ans)
    return
prime()
solve()