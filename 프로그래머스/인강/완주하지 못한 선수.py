def solution(participant, completion) :
    #두개의 배열을 비교하기 위해 정렬
    participant.sort()
    completion.sort()
    
    #두개의 배열을 비교하고 다른 값을 리턴
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]
    
    #완주하지 못한 선수가 맨 뒤에 있을경우 for문에 들어가지 않고 나오므로
    return participant[-1]

print(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))