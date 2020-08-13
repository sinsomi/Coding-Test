t=int(input())
ans=[list(map(lambda x: x[::-1], input().split())) for _ in range(t)]
for words in ans:
    #리스트 안의 요소들을 문자열로 한꺼번에 출력해주는 '*'
    print(*words)