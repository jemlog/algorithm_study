lists = list(input()) # 문자열 입력을 바로 list로 만들때 사용
for i in range(len(lists)):
    if ord(lists[i]) < 68 :
        lists[i] = chr(int(ord(lists[i]))+23)
    else:
        lists[i] = chr(int(ord(lists[i])) -3)
print("".join(lists))
