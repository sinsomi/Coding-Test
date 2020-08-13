import sys

n=int(input())
alpha=[0]*26
i=0

for i in range(n):
    #각 알파벳을 입력받아서 젤 뒤의 수부터 인덱스와 함께 뽑아옴
    for j,c in enumerate(input()[::-1]):
        #alpha 리스트에 해당 문자의 아스키코드에다가 10의 인덱스만큼 제곱근한것을 곱함
        alpha[ord(c)-ord('A')]+=(10**j)

#alpha리스트를 큰순서대로 정렬(9부터 차례로 곱해주기위해)
alpha.sort(reverse=True)

#alpha리스트의 i번째가 있다면 해당하는 숫자에 9-i를 곱하여 더함
#단어의 개수가 최대 10개이므로 10번반복
ans=0
for i in range(10):
    if alpha[i]:
        ans+=(alpha[i]*(9-i))

print(ans)