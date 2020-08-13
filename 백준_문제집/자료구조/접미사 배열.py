import sys

word=sys.stdin.readline()
word_end=[]
#word를 처음부터끝까지, 두번쩨부터끝까지 ... 이런식으로 잘라옴
for i in range(len(word)-1):
    # word_end리스트에 저장
    word_end.append(word[i:-1])
#정렬
word_end.sort()
for i in word_end:
    print(i)