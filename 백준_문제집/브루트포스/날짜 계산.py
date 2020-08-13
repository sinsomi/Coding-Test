E, S, M = map(int, input().split())
year = 1
#년도는 1년부터 시작
#(년도 - E)는 15, (년도 - S)는 28, (년도 - M)는 19로 나누어 떨어지면 출력
#1년씩 증가해가면서 확인
while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        print(year)
        break
    #년도는 while문 돌때마다 1씩 증가
    year += 1