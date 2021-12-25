hab = 0
while True :
    print('정수 입력')
    dab = int(input())
    hab = hab + dab
    if dab == 0 :
        print('합은 {0}입니다.'.format(hab))
        break
