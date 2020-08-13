n = int(input())
#ans는 자릿수
ans, i = 0, 1
while i <= n:
    #1번 while: i=1이므로 일의자리수를 ans에 저장해주는 과정
    #2번 while: i=10이므로 십의자리수를 ans에 저장해주는 과정
    #3번 while: i=100이므로 백의자리수를 ans에 저장해주는 과정
    #...i가 n보다 작거나 같을때까지 반복
    ans += (n-i+1)
    i *= 10
print(ans)