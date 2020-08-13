n= int(input())
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
ans=0

#i는 행
def solve(i):
    global ans
    if i==n:
        ans+=1
        return
    #j는 열
    for j in range(n):
        #셋중에 하나가 방문하지 않은 곳이라면
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j],b[i+j],c[i-j+n-1]=True,True,True
            #행을 증가시켜서 비교
            solve(i+1)
            a[j],b[i+j],c[i-j+n-1]=False,False,False

solve(0)
print(ans)