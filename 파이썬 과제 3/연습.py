name = ['박훈희','정수현','김수진']
course=['국어','영어','수학']
grade = [80,50,60]
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
    if i == len(name):
        break
print(name)
print(course)
print(grade)
print(find)
print(rank)
print(iindex)

