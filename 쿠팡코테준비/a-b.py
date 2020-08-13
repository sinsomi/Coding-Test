a,b=map(int,input().split())
cnt=0

while True:
    if b<a:
        cnt=-1
        break
    if a==b:
        cnt+=1
        break
    if b%10==1:
        cnt+=1
        b//=10
    elif b%2==0:
        cnt+=1
        b//=2
    else:
        cnt=-1
        break
print(cnt)