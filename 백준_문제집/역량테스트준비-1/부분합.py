import sys

n,m=map(int,input().split())
nums=list(map(int,sys.stdin.readline().split()))

def solve():
    left=right=k=s=0
    ans=1000001
    while True:
        #구해야하는 합보다 커지면 left포인터를 증가
        if s>=m:
            ans=min(ans,k)
            s-=nums[left]
            left+=1
            k-=1  #왼쪽포인터가 움직일땐 숫자의 길이가 줄어듬
        #아닐땐 right포인터를 차례로 증가
        else:
            if right==n:
                break
            s+=nums[right]
            right+=1
            k+=1   #오른쪽포인터가 움직일땐 숫자의 길이가 늘어남
    if ans!=1000001: print(ans)
    else: print(0)
    return
solve()