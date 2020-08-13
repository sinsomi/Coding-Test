n = int(input())
port_list = list(map(int, input().split()))
tmp_list = [-1]
ans = 0

#자리찾는 함수
#arr가 정렬된 상태로 유지하면서 val이 삽입될 수 있는 위치중 가장 작은 인덱스 위치
def lower_bound(arr, val): 
    start=0
    end=len(arr)-1 
    #시작인덱스와 끝인덱스가 만나는 지점까지 반복
    while start <= end: 
        m = (start+end)//2 
        #만약 arr의 중값인덱스값이 해당값보다 크면, end값을 (중간인덱스-1) 해줌
        if arr[m] > val: 
            end = m-1 
        else: 
            start = m+1 
    return start

for i in range(n):
    #만약에 tmp리스트의 마지막값이 port리스트의 i번째 값보다 작으면
    #tmp리스트에 집어넣고, ans는 증가
    if tmp_list[-1] < port_list[i]:
        tmp_list.append(port_list[i])
        ans += 1
        print(tmp_list,'append')
    #port리스트의 i번째값이 더 작다면 걍 교체
    else:
        tmp_list[lower_bound(tmp_list, port_list[i])] = port_list[i]
        print(tmp_list, 'lower_bound')

print(ans)