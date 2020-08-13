n = int(input())
a = list(map(int, input().split()))

def next_permutation(a):
    n=len(a)-1
    i = n
    j = n
    #맨끝부터 비교해서 내려오는데
    #i가 0보다 크고, 리스트가 끝에서부터 내림차순이면
    #-1씩 감소
    while i>0 and a[i-1]>=a[i]:
        i-=1
    #만약 i가 0이라면 리스트가 끝에서부터 완전한 오름차순이므로
    #즉 리스트자체가 완벽한 내림차순이므로 False리턴
    if i==0:
        return False
    #여기서 i는 끊긴지점의 i이다
    #j는 다시 맨끝원소
    #a[i-1]이 a[j]보다 클경우가 있으면 게속j를 감소
    #값을 swap
    while a[i-1]>=a[j]:
        j-=1
    a[i-1],a[j]=a[j],a[i-1]
    #그이후의 값들을 정렬
    j=n
    while i<j:
        a[i],a[j]=a[j],a[i]
        i+=1
        j-=1
    return True

if next_permutation(a) is True:
    for i in a:
        print(i, end=' ')
    print()
else:
    print(-1)


