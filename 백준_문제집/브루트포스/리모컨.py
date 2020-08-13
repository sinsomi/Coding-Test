import sys

#이동하려는 채널, 고난장 버튼 개수, 고장난 버튼 입력받아옴
n=int(input())
m=int(input())
break_btn=sys.stdin.readline().split()
#전체 버튼 btn
btn=list(map(str,[p for p in range(10)]))
current_btn=[]
#고장난 버튼을 뺀 사용가능버튼 current_btn
for i in btn:
    if i not in break_btn:
        current_btn.append(i)
#이동하려는 채널과 수빈이 채널의 차 => 우리가 만들어야 할 수
result = abs(n - 100)

# 500001이어도 될거같은뎅 왜 이만큼돌지 ㅇ_ㅇ..? 여튼 하나씩 돌아봄
for i in range(1000001):
    is_true = True
   # 지금 수를 string으로 만들어서 하나씩 접근해봄
    for part_num in str(i):
      # 만약에 현재 수 중에 사용할 수 없는 버튼이 있으면
        if part_num not in current_btn:
            #False로 바꿔줌
            is_true = False
            #더이상 for문을 돌 필요가 없음 --> 이미 사용할 수 없는 버튼을 포함하고 있기 때문에
            break
    #is_true가 False이기 때문에 result를 업데이트 하지않고 다시 for문을 돌러 간당
    if is_true is True:
        result = min(result, abs(n - i) + len(str(i)))

print(result)