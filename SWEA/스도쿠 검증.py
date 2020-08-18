import sys

maps=[list(map(int,[p for p in sys.stdin.readline().split()])) for _ in range(9)]

#가로
def hori():
    ans=0
    for i in range(9):
        nums = list(range(1, 10))
        cnt = 0
        for j in range(9):
            if maps[i][j] in nums:
                nums.remove(maps[i][j])
                cnt+=1
            else:
                return False
        if cnt==9:
            ans+=1
    if ans==9:
        #print('가로','True')
        return True
    return False

#세로
def verti():
    ans=0
    for i in range(9):
        nums = list(range(1, 10))
        cnt=0
        for j in range(9):
            if maps[j][i] in nums:
                nums.remove(maps[j][i])
                cnt+=1
            else:
                return False
        if cnt==9:
            ans+=1
    if ans == 9:
        #print('세로', 'True')
        return True
    return False

#3x3
def bythree():
    ans=0
    for x in range(0,7,3):
        for y in range(0,7,3):
            nums = list(range(1, 10))
            cnt=0
            for i in range(3):
                for j in range(3):
                    if maps[i+x][j+y] in nums:
                        nums.remove(maps[i+x][j+y])
                        cnt+=1
            if cnt==9:
                ans+=1
    if ans==9:
        #print('3x3', 'True')
        return True
    return False

if hori() and verti() and bythree():
    print(1)
else:
    print(0)