n=int(input())
i=1
cnt=0
while True:
    if n-i>=0:
        n-=i
        cnt+=1
        i+=1
    else:
        print(cnt)
        break