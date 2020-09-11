def solution(n):
    ans=''
    while n>0:
        n-=1
        ans='124'[(n%3)]+ans
        n//=3
    return ans
print(solution(10))