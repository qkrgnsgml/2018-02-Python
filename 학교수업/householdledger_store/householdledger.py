import os
import datetime
path = "c:\\householdledger"

def WriteDiary() :
    print("오늘의 지출내역(종료시:... 입력)")
    lines = []
    with open(os.path.join(path, datetime.datetime.now().strftime("%Y-%m-%d.txt")), 'w') as file :
        while(True) :
            content = input("내역:")
            if content == '...' : break;
            money = input("금액:")
            lines.append("{0}|{1}\n".format(content,money))
        if len(lines) > 0 :
            file.writelines(lines)
    print("입력 종료")
        
def ViewDiary() :
    filenames = os.listdir(path)        
    list = []
    if len(filenames) > 0 :            
        for i in range(len(filenames)) :
            name = filenames[i]
            ext = os.path.splitext(name)
            if ext[-1] != '.txt' : continue            
            list.append(os.path.join(path, name))
            print("[{0}]{1}".format(i+1, name))
            
        with open(list[int(input("번호선택"))-1]) as file :
            tmoney = 0;
            for line in file :
                cm = line.strip().split('|')
                tmoney += int(cm[1])
                print("{0}:{1}".format(cm[0], cm[1]))
            print("="* 30)
            print("지출금액 :", tmoney)
    else :
        print("작성한 지출내역 없음")
            
if __name__ == '__main__' : 
    while(True) :
        print("1.오늘 지출")
        print("2.지난 지출")
        print("3.나가기")

        menu = int(input("메뉴선택:"))
        if menu == 3 : break;
        elif menu == 1 : WriteDiary()                  
        elif menu == 2 : ViewDiary()

        print("\n")
