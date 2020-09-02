n,k=map(int,input().split())
words=[]
for i in range(n):
    words.append(input().strip())
for i in range(len(words)):
    if 'anta' and 'tica' in words[i]:
        words[i]=words[i].replace('anta','')
        words[i]=words[i].replace('tica','')
    else:
        words.remove(words[i])

#anta,tica를 지우고 문자열이 짧은 순대로 정렬
words=sorted(words,key=lambda x:len(x))

words_cnt=0
word_cnt=0
for word in words:
    word_cnt+=len(word)
    if word_cnt>k:
        print(words_cnt)
        break
    words_cnt+=1