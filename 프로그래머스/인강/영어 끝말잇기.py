def solution(n,words):
    ans=[]
    case=1
    person=0
    for i in range(len(words)):
        if i==0:
            person+=1
            ans.append(words[i])
            continue
        if person==n:
            person=0
            case+=1
        if words[i] not in ans:
            if words[i][0]==words[i-1][-1]:
                print(words[i][0],words[i-1][-1])
                person+=1
                print(person)
                ans.append(words[i])
            else:
                person+=1
                return [person,case]
        elif words[i] in ans:
            person+=1
            return [person,case]

    return [0,0]
print(solution(3,['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))