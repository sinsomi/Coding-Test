n=int(input())
num=1
cnt=0

while True:
    sorted_i = ''
    if cnt==n:
        break
    for i in sorted(str(num),reverse=True):
        if sorted_i.count(i)>=1:
            break
        sorted_i+=i
    if str(num)==sorted_i:
        ans=num
        cnt+=1
    num+=1
print(ans)
