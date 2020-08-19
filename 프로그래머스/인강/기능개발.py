def solution(progresses,speeds):
    #days는 각 기능개발이 몇일 걸리는지 저장하는 리스트
    days=[]
    #speed만큼 더해주면서 100을 넘기는 지점의 날짜를 리턴해서 days에 저장
    for i in range(len(progresses)):
        s=progresses[i]
        cnt=0
        while s<100:
            s+=speeds[i]
            cnt+=1
        days.append(cnt)

    #days
    ans=1
    fun_cnt=[]
    i=1
    while days:
        if len(days)==1:
            fun_cnt.append(ans)
            days.pop()
        #다음원소가 작을경우 다음원소제거하고 ans증가
        elif days[i-1]>=days[i]:
            ans+=1
            days.pop(i)
        #다음원소가 클경우 이전원소제거하고 ans를 리스트에 저장시키고 ans초기화
        else:
            fun_cnt.append(ans)
            days.pop(i-1)
            ans=1

    return fun_cnt

print(solution([93,30,55],[1,30,5]))