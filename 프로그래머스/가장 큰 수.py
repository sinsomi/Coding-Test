def solution(numbers):
    ans=''
    numbers=list(map(str,numbers))
    #문자열을 3번씩 나열한것을 기준으로 정렬
    numbers.sort(key=lambda x:x*3,reverse=True)
    return ''.join(numbers)

print(solution([3, 30, 34, 5, 9]))