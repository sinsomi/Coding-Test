def solution(scoville,K):
    cnt=0

    while min(scoville)<K:
        if len(scoville)==1 and scoville[0]<K:
            return -1

        scoville=sorted(scoville,reverse=True)
        scoville.append(scoville.pop()+scoville.pop()*2)
        cnt+=1

    return cnt
print(solution([1, 2, 3, 9, 10, 12],7))