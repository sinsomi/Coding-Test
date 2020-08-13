n=int(input())
ans=[]
#n이 1이면 종료(1은 소인수분해x)
while n!=1:
    #i는 2부터 n까지
    for i in range(2,n+1):
        if n%i==0:
            ans.append(i)
            n=n//i
            break
for i in ans:
    print(i)