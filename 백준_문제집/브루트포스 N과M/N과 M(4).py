import itertools

n,m=map(int,input().split())
nums=[i for i in range(1,n+1)]
#여기 for문은 중복조합을 만들어줌
for num in itertools.combinations_with_replacement(nums,m):
    for i in num:
        print(i,end=' ')
    print(end='\n')