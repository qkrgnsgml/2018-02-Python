class Score :
    ratio = {"mid":30, "fin":30, "hw":20, "att":20}

    def __init__(self):
        self.mid = 30
        self.fin = 30
        self.hw = 20
        self.att = 20

    def total(self) :
        self.total = self.mid + self.fin + self.hw + self.att
        return self.total

    def grade(self):
        if self.total>=90:
            self.grade="A"
        elif self.total>=80:
            self.grade="B"
        elif self.total>=70:
            self.grade="C"
        elif self.total>=60:
            self.grade="D"
        else:
            self.grade="F"
        return self.grade

    def setScore(self,name,score,cri=100) :
        if name=="mid":
            self.mid=score*(self.ratio["mid"]/cri)
        elif name=="fin":
            self.fin=score*(self.ratio["fin"]/cri)
        elif name=="hw":
            self.hw=score*(self.ratio["hw"]/cri)
        elif name=="att":
            self.att=score*(self.ratio["att"]/cri)

def rank(s_dic) :
    dic={}
    for k,v in s_dic.items():
        dic[v.total]=k
    sort=sorted(dic.items(),reverse=True)
    j=0
    for i in range(0,3):
        print("{0}: {1}".format(j+1,sort[i]))
        j+=1
    # 랭크에서 딕셔너리 안에 키랑 밸류 따로 포문으로 빼서 정렬하는게 잘 안돼서..
    # 그냥 포문으로... ㅠ 순위는 정렬되지만 교수님이랑 형태가 다름

if __name__ == "__main__":
    score_list = {}
    score_list["김아영"] = Score()
    score_list["최미소"] = Score()
    score_list["윤선영"] = Score()

    print("#1")
    score_list["김아영"].setScore("mid",70)
    score_list["김아영"].setScore("fin",80)
    score_list["김아영"].setScore("hw",100)
    score_list["김아영"].setScore("att",100)
    score_list["최미소"].setScore("mid",30,30)
    score_list["최미소"].setScore("fin",28,30)
    score_list["최미소"].setScore("hw",20,20)
    score_list["최미소"].setScore("att",20,20)
    score_list["윤선영"].setScore("mid",40,50)
    score_list["윤선영"].setScore("fin",20,50)
    score_list["윤선영"].setScore("hw",100)
    score_list["윤선영"].setScore("att",100)

    print("#2")
    for k,v in score_list.items():
        print("이름:{0} 총점:{1} 학점:{2}"
                  .format(k,v.total(),v.grade()))
    print("#3")
    rank(score_list)
