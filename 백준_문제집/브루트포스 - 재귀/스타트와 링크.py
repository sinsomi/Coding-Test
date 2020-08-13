from itertools import combinations
import math

n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]

min_ans=math.inf  #min_ans에 젤 초기값은 무한대값으로 설정

#두 팀으로 나눌 수 있는 경우의 수
for case in combinations(range(1, n + 1), n // 2):
    s1 = s2 = 0
    #모든 경우에 해당하는 좌표를 각각 i,j
    for i in case:  # 1팀 점수
        for j in case:
            s1 += datas[i - 1][j - 1]

    res = set(range(1, n + 1)) - set(case)  # 2팀 점수
    #모든 경우에 해당하는 좌표를 각각 i,j
    for i in res:
        for j in res:
            s2 += datas[i - 1][j - 1]
    min_ans = min(min_ans, abs(s1 - s2))
print(min_ans)