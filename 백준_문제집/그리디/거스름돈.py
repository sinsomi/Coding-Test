#지불해야하는돈
money=int(input())

#거스름돈
change = 1000 - money

#거스름돈종류
change_money=[500,100,50,10,5,1]

#동전개수
num=0

#큰값이 있는 뒤의 인덱스부터 계산
for i in range(6):
    coin = change_money[i]
    if change >= change_money[i]:
        temp = change//coin
        change -= coin*temp
        num += temp
print(num)