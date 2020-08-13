import math
def is_prime(num):
    if num == 1: return False
    #n은 num의 제곱근
    n = int(math.sqrt(num))
    # 2부터 n까지 나누어 떨어지는지 확인
    for i in range(2, n+1):
        #나누어떨어지면 소수가 아님
        if num%i == 0: return False
    return True
# main
m, n = map(int, input().split())
for i in range(m, n+1):
    if is_prime(i): print(i)