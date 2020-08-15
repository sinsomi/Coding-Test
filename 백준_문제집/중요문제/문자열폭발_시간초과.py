string=input().strip()
explo=input().strip()

while explo in string:
    if len(explo)>len(string):
        break
    if explo in string:
        string=string.replace(explo,'')

if len(string)==0:
    print('FRULA')
else:
    print(string)