def year(m, n, x, y):
    m_test = 0
    n_test = 0
    cnt = 0
    while True:
        if x < m:
            m_test += 1
            if m_test > m:
                m_test = 1  # m_test가 m과 같아지면 다시 1로 돌리기
            if y < n:
                n_test += 1
                if n_test > n:
                    n_test = 1
            cnt += 1

            if x == m_test and y == n_test:
                return cnt
            if cnt > m * n:  # m*n인 종말의 해보다 높은값이 나오면 안됨
                return -1


for i in range(int(input())):
    m, n, x, y = map(int, input().split(' '))
    print(year(m, n, x, y))