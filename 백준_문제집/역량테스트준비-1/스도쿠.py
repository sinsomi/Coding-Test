import sys

sudoku=[list(map(int,sys.stdin.readline().split())) for _ in range(9)]
zeros=[]
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            zeros.append([i,j])

def is_possible(i,j):
    nums=[1,2,3,4,5,6,7,8,9]
    
    #행,열 검사
    for k in range(9):
        if sudoku[i][k] in nums:
            nums.remove(sudoku[i][k])
        if sudoku[k][j] in nums:
            nums.remove(sudoku[k][j])
    
    #정사각형 검사 -이부분식이 잘이해안감
    i//=3
    j//=3
    for p in range(i*3,(i+1)*3):
        for q in range(j*3,(j+1)*3):
            if sudoku[p][q] in nums:
                nums.remove(sudoku[p][q])
    return nums

flag=False
def dfs(x):
    global  flag

    #이미 답이 출력된 경우(재귀를 사용할때는 이미 답이 출력되면 다시 이과정을
    #반복하지 않도록 flag를 설정해줌
    if flag:
        return

    #마지막 0까지 다채웠을경우
    if x==len(zeros):
        for row in sudoku:
            print(*row)
        #답출력
        flag=True
        return
    
    else:
        [i,j]=zeros[x]
        possible=is_possible(i,j) #가능한 숫자들을 받음

        for num in possible:
            sudoku[i][j]=num #가능한 숫자 중 하나를 넣어줌
            dfs(x+1) #다음 0으로 넘어감
            sudoku[i][j]=0 #초기화 (정답이 없을 경우를 대비) -이부분도 잘이해안감

dfs(0)