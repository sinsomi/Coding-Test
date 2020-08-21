def solution(clothes):
    nums=[]
    #각가지수의 경우(종류의 갯수만큼 곱해줌)
    #모자가2개 상의가 3개면 2x3=6가지
    while clothes:
        kwd=clothes[0][1]
        tmp=list(filter(lambda x:x[1]==kwd,clothes))
        nums.append(len(tmp)+1)    #각 아이템이 빠질수있는 경우까지 하나더더해준다.
        for i in tmp:
            clothes.remove(i)

    #(각 가지수+1)한 값들이 담긴 nums안에 수들을 곱해준다
    ans=1
    for i in nums:
        ans*=i

    #아이템을 아무것도 착용하지 않은 1가지경우 빼주기
    return ans-1

print(solution([['a','face'],['b','face'],['d','상의'],['f','상의'],['w','상의'],['c','안경']]))
#print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))