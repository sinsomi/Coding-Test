#k번째 해 즉, 정답이 k이면
#k-x에 m을 나누면 나머지가 0이다
#k-y에 n을 나누면 나며지가 0이다
#즉, 정답 k는 x와 y에 m과 n을 계속 더한 값중 하나이다
#x에 m을 계속더해주고 y를 뺀값에 n이 나누어 떨어지면 그값이 정답 - 이부분 이해안감

def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))