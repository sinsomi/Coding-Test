def solution(phone_book):
    for i in range(len(phone_book)-1):
        for j in range(i+1,len(phone_book)):
            if len(phone_book[i])<=len(phone_book[j]):
                if phone_book[i]==phone_book[j][:len(phone_book[i])]:
                    return False
            else:
                if phone_book[i][:len(phone_book[j])]==phone_book[j]:
                    return False
    return True

print(solution(['119','123','333']))