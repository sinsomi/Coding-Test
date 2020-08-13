import sys
input_str=sys.stdin.readline().strip()
#답을 구해주는 함수
def solution(arrangement):
    #answer는 쇠막대기 수
    answer = 0
    #stack리스트를 만듬
    stick_stack = []
    #인접한()에 대해서 '*'문자열로 바꾼 문자열 for문 실행 => 레이저를 *로 바꾼코드
    for value in arrangement.replace('()','*'):
        #만약 value가 (이면 , 쇠막대기 시작이므로
        if value == '(' :
            #answer를 증가
            answer += 1
            #value를 스택에 추가 => 막대기시작점하나를 추가
            stick_stack.append(value)
        #만약 막대기의 끝이면, 스택리스트에 pop() => 즉 젤첨 들어온 (를 제거.
        elif value == ')' : stick_stack.pop()
        #레이저를 만나면 레이저가 자르려는 스택의 길이만큼 더해줌
        #쇠막대기 1개를 1번자르면 2개, 쇠막대기 2개를 1번자르면 4개
        else : answer += len(stick_stack)
    return answer

print(solution(input_str))