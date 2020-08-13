import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    s = [0 for i in range(n + 1)]
    for j in range(n):
        a, b = map(int, input().split())
        s[a] = b
    min_n = s[1]
    cnt = 0
    for k in range(2, n + 1):
        if s[k] > min_n:
            cnt += 1
        else:
            min_n = s[k]
    print(n - cnt)

#서류심사 성적을 기준으로 오름차순으로 설정한다.
#그리고 면접성적만 확인하면서 검사를 해나가는데
#min_n보다 작은 값이 있다면 min_n에 저장해주고
#min_n보다 크다면 cnt를 증가시켜준다.
