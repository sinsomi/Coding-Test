def solution(prices):
    ans=[]
    #prices의 원소 i와 i이후의 원소들을 비교해서 같거나 크면 cnt를증가
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                cnt+=1
            #i이후의 원소들중 작아지는 지점을 만나면 1을증가하고(1초는유지된것이므로) break
            else:
                cnt+=1
                break
        ans.append(cnt)
    #맨마지막원소는 고정으로 0
    ans.append(0)
    return ans

print(solution([1, 2, 3, 2, 3, 3, 1]))