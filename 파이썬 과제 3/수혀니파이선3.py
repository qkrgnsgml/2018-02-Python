class Score :
    ratio = {"mid":30, "fin":30, "hw":20, "att":20}

    def __init__(self):
        self.mid = 0
        self.fin = 0
        self.hw = 0
        self.att = 0

    def total(self):
        self.tot=self.mid+self.fin+self.hw+self.att
        return self.tot

    def grade(self):
        if self.tot>=90:
            self.grade="A"
        elif self.tot>=80:
            self.grade="B"
        elif self.tot>=70:
            self.grade="C"
        elif self.tot>=60:
            self.grade="D"
        else:
            self.grade="F"
        return self.grade
        

    def setScore(self,obj,score,cri=100) :
        if obj=="mid":
            self.mid=self.ratio["mid"]*(score/cri)
        elif obj=="fin":
            self.fin=self.ratio["fin"]*(score/cri)
        elif obj=="hw":
            self.hw=self.ratio["hw"]*(score/cri)
        elif obj=="att":
            self.att=self.ratio["att"]*(score/cri)
        
    

def rank(score_dic) :
    dic={}
    for k,v in score_dic.items():
        dic[v.tot]=k
    sort=sorted(dic.items(),reverse=True)
    j=0
    for i in range(0,3):
        print("{0}: {1}".format(j+1,sort[]))
        j+=1


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
