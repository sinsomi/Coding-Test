import sys
T = int(sys.stdin.readline())
MAX = 1000000
check = [False, False] + [True] * (MAX-1)
primes = []
prime_count = 0
for i in range(1, MAX+1):
    if check[i]:
        primes.append(i)
        prime_count += 1
        for j in range(i*2, MAX+1, i):
            check[j] = False
for _ in range(T):
    N = int(sys.stdin.readline())
    result = 0
    for i in range(1, prime_count):
        #두 소수를 A,B라고 했을때 A가 A <= B 보다 작을때만 참
        if primes[i] <= N - primes[i]:
            if check[N-primes[i]] == True:
                result += 1
        #A가 B보다 크다면 자리가 바뀐 소수가 나오기 시작하는 것이기 때문에 그때 break
        else:
            break

    print(result)