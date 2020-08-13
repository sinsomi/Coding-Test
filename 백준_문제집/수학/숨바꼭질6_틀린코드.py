import sys
n,s=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
ans=[]
max_gcd=0
#최대공약수 함수
def gcd(x,y):
    while(y):
        x,y= y,x%y
    return x
#수빈이의 위치와 동생들의 위치의 차(절댓값)
for i in range(n):
    ans.append(abs(s-a[i]))
for i in range(len(ans)-2):
    max_gcd=gcd(gcd(ans[i],ans[i+1]),ans[i+2])
#만약 최대공약수가 없으면
if max_gcd==0:
    #절대값의 차 중에서 가장 적은 것(이렇게 하면 안됨..)
    print(min(ans))
else:
    print(max_gcd)