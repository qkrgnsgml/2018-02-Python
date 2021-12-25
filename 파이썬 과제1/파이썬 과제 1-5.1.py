dic= {}
while True:
    print("[입력모드]이름을 입력해주세요")
    a = input()
    if a == '':
        print("[검색모드]이름을 입력해주세요")
        a = input()
        for k, v in dic.items():
            if dic[a] == dic[k]:
                print("{0}의 전화번호는 {1} 입니다.".format(k,v))
                break  
    print("전화번호를 입력해주세요")
    b = input()
    dic[a]=b
