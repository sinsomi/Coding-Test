import sys
n=int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))
ans=[]
#소수인지 아닌지 판별하는 함수
def is_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i == 0:
            count+=1
    if count==2:
        return True
    return False
#각각의 숫자들에 대해 구해주기
for n in nums:
    ans.clear()
    # 두 소수의 합의 최소 = 4 이면서 짝수이면
    if n >= 4 and n % 2 == 0 :
        # i는 2부터 n/2까지
        for i in range(2, int(n/2) + 1):
            #소수면
            if is_prime(i) == 1 and is_prime(n - i) == 1 :
                #ans에다가 소수쌍을 저장
                ans += [[i, n - i]]
    print(len(ans))