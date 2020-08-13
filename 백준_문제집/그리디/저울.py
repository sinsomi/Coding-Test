n=int(input())
j_list=list(map(int, input().split()))
j_list.sort()
s=0  #저울추 무게의 합

for i in range(n):
    #저울추무게의 합에 1씩더해가면서 빈공간을 확인
    #저울추무게합에 1을 더한값이 저울추자체보다 작을 경우 break
    if s+1 < j_list[i]:
        break
    #아닐 경우 측정할수 있는 값이므로 저울추만큼 더해준다
    s=s+j_list[i]

print(s+1)    #s+1을 측정할 수 없으므로 출력