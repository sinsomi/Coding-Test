import sys

num=int(input())
#2의개수
two=0
#3의개수
five=0
#n은 1부터 num까지(소인수분해를 통해 각 수가 가지고 있는 2와 5가 몇개있는지알아야하므로)
for n in range(1,num+1):
    while n%2 == 0:
        two+=1
        n=n//2
    while n%5 == 0:
        five+=1
        n=n//5
#2와 5의 개수중 더 작은걸 출력하면 10의 쌍이다.
print(min(two,five))