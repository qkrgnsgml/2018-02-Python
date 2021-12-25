def totalprint(score_list):
    find=[]
    rank=[]
    iindex=[]
    for i in range(len(name)):
        find.append(grade[i])
        rank.append(grade[i])
    rank.sort(reverse = True)
    for i in range(len(name)):
        iindex.append(find.index(rank[i]))
    i = 0
    while True:
        print("이름: {0} 과목: {1} 평균: {2}".format(name[iindex[i]],course[iindex[i]],grade[iindex[i]]))
        i = i + 1
        if i == score_list:
            break

#3-2번에서 정렬햇던 방법 더 응용해서 복잡하게 만드니까 나오기는 하는데...
#너무 어거지고... ㅠ 일단 성공...!

name = []
course = []
grade = []
while True:
    print("성적을 입력하시겠습니까?(Y,N)",end = "")
    dab = input()
    if dab == "Y":
        print("이름:",end = "")
        a = input()
        if name.count(a)>0:
            b = name.index(a)
            print("과목:",end = "")
            d = '/' + input()
            course[b] = course[b] + d
            print("성적:",end = "")
            c = int(input())
            grade[b] = (grade[b] + c) / 2
            continue
        #이 이프문으로 하면 과목 2개까지는 평균 낼 수 있는데 3개부터는 안돼요 ㅠㅠ
        #다른 방법은... ㅠ
        name.append(a)
        print("과목:",end = "")   
        course.append(input())
        print("성적:",end = "")
        grade.append(int(input()))
    elif dab == "N" :
        if len(name) == 0:
            print("입력한 성적이 없습니다.")
            break
        else:
            totalprint(len(name))
            break
            

    
