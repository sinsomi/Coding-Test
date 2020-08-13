#최대공약수 함수
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

n,s = map(int, input().split())
location = list(map(int, input().split()))
distance = []

#수빈이의 위치와 동생들의 위치의 차(절댓값)
for i in location:
    distance.append(abs(i-s))

#위치의 차의 첫번째값을 result에 저장
result = distance[0]

#gcd(distance[1], distance[1])
#gcd((distance[1]과 distance[1]의 gcd),distance[2])
for idx in range(1, n):
    result = gcd(result, distance[idx])

print(result)