import sys
nums=[]
ans=[]
real_ans=[]
#입력받아오는 부분_0을 입력 받으면 종료
while(True):
    n=int(input())
    if n==0:
        break
    else:
        nums.append(n)
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
    # 두 소수의 합의 최소 = 4
    if n >= 4 and n % 2 == 0 :
        for i in range(2, int(n/2) + 1):
            if is_prime(i) == 1 and is_prime(n - i) == 1 :
                #ans에다가 소수쌍을 저장
                ans += [[i, n - i]]
    #ans에 저장된 소수쌍중 차이가 가장큰 것을 구하는 코드
    temp=0
    for i in range(len(ans)):
        if temp < (ans[i][1] - ans[i][0]):
            temp = (ans[i][1] - ans[i][0])
            #차이가 가장 크면 real_ans에 저장
            real_ans=[ans[i]]
    #출력
    for i in range(len(real_ans)):
        print(n,' = ',real_ans[i][0],' + ',real_ans[i][1])