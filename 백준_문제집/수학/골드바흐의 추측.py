MAX = 1000000
prime = [False for _ in range(MAX+1)]
#우선 2부터 1,000,000까지의 모든 소수를 에라토스테네스의 체로 구함
for i in range(2, MAX+1):
    if i*i > MAX:
        break
    if prime[i] is False:
        #i의 배수들은 True로 바꿈=>소수가 아니면 True
        for j in range(i*i, MAX+1, i):
            prime[j] = True

while True:
    n = int(input())
    if n is 0:
        break
    for i in range(2, MAX+1):
        #prime[i]가 소수일때만, j=n-i 를 입력
        if prime[i] is False:
            j = n - i
            #prime[j]가 소수일때만
            if prime[j] is False:
                print(n, "=", i, "+", j)
                break