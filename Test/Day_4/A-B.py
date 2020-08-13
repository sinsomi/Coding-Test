a,b=map(int,input().split())
ans=0
while True:
    if b<a:
        ans=-1
        break
    if a==b:
        ans+=1
        break
    if b%10==1:
        ans += 1
        b//=10
    elif b%2==0:
        ans += 1
        b//=2
    else:
        ans=-1
        break
print(ans)