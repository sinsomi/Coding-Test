#재귀, 시간복잡도 O(2^N) ->함수가 한 번 호출되면 다시 두 번 호출되기 때문에 지수적으로 증가
#값이 저장되지 않고 계속 같은 함수를 중복해서 재귀호출함
def fibo1(n):
    return fibo1(n-1)+fibo1(n-2) if n>=2 else n


#반복, 시간복잡도 O(N) ->  n이 2이상일 때는 n-1 번만큼 반복문을 시행
def fibo2(n):
    if n<2:
        return n

    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return b


#DP(메모이제이션), 시간복잡도 O(N)
#cache를 만들어 cache에 recursion을 저장시켜 놓으면 됨
memo={0:0,1:1}

def fibo3(n):
    if n not in memo:
        memo[n]=fibo3(n-1)+fibo3(n-2)
    return memo[n]
fibo3(5)

