dict = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 10진법이면 9 까지, 36진법이면 Z까지 표현된다
n, b = map(int, input().split())
answer = ''

while n != 0:
    # 위치로 진법 변환
    # b로 나눈 나머지를 answer에 저장
    answer+=str(dict[n%b])
    n //= b
#answer에 저장된 반대순서로 출력해야함
print(answer[::-1])