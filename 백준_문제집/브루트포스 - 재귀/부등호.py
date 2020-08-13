#(부등호갯수+1)만큼 permutation으로 순열만들고
#그순열에 대해서 부등호 성립하는지 확인.
#성립하면 max,min갱신

n = int(input())
op = input().split()
c = [False]*10 #수를 중복하면 안되므로 별도로 사용여부를 따져주는 리스트
mx, mn = "", ""

def possible(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

#하나의 숫자를 구하기 위해서 입력으로 주어진 길이(N)+1 만큼 재귀 함수를 호출
#permutation만들어주는 함수와 같다고 보면됨.
def solve(depth, s):
    global mx, mn
    #재귀 함수 종료 조건 : 숫자 개수(길이) == N+1
    if depth == n+1:
        if not len(mn):
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        #i가 방문하지 않았으면
        if not c[i]:
            #cnt가 0이거나, 다음 숫자가 부등식에 맞으면
            if depth == 0 or possible(s[-1], str(i), op[depth-1]):
                #i를 방문했다고 고치고
                c[i] = True
                #재귀호출
                solve(depth+1, s+str(i))
                #다시 방문하지 않았다고 고침
                c[i] = False

solve(0, "")
print("%s\n%s" % (mx, mn))