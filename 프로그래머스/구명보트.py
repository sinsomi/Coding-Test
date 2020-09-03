def solution(people, limit):
    cnt=len(people)
    people.sort(reverse=True)
    start,end=0,len(people)-1
    while start<end:
        #print(people[start],people[end])
        if people[start]+people[end]<=limit:
            end-=1
            cnt-=1
        start+=1
    return cnt

print(solution([70, 50, 80, 50],100))
