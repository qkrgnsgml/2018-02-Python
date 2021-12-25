class Product :
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.su = 0
        self.money = 0

    def buy(self,num = 1):
        if self.stock < num:
            print("{0}의 판매할 재고 수량이 없음".format(self.name))
        else:
            print("{0}의 총 판매가격은 {1}원 구매하겠습니까(Y/N)?".format(self.name,num*self.price), end = "")
            dab = input()
            if dab == "N":
                pass
            elif dab == "Y":
                print("{0}제품 {1}개 총 {2}원에 판매하였습니다.".format(self.name,num,num*self.price))
                self.stock = self.stock - num
                self.su = self.su + num
                self.money = self.money + num*self.price

    def currentState(self):
        print("제품명:{0} 단가:{1} 재고:{2}".format(self.name,self.price,self.stock))

    def totalState(self):
        print("제품명:{0} 총 판매 수량:{1} 총 판매 금액:{2}".format(self.name,self.su,self.money))

def rankTotalPrice(*p_list):
    find=[]
    rank=[]
    for i in range(0,4,1):
        find.append(product_list[i].money)
        rank.append(product_list[i].money)
    rank.sort(reverse = True)
    one = find.index(rank[0])
    two = find.index(rank[1])
    three = find.index(rank[2])
    four = find.index(rank[3])
    print("1 : {0} / {1}". format(product_list[one].name,rank[0]))
    print("2 : {0} / {1}". format(product_list[two].name,rank[1]))
    print("3 : {0} / {1}". format(product_list[three].name,rank[2]))
    print("4 : {0} / {1}". format(product_list[four].name,rank[3]))
    #for i in range(0,4,1):
        #print("{0} : {1}".format(i,rank[i]))
    #위에 포문으로 하려햇는데 잘 안돼서 일일히 노가다로.. 길게 해서 순위별로는
    #나왔는데.. 너무 길어져서 교수님은 어떻게 하셧는지 궁금합니다!

if __name__ == "__main__":
    product_list = [Product(name="연필", price=1000,stock = 10)
                    , Product(name="샤프", price=3000,stock = 5)
                    , Product(name="공책", price=2000,stock = 5)
                    , Product(name="볼펜", price=2000,stock = 5)]
    print("#1"); product_list[0].buy()
    print("#2"); product_list[0].buy()
    print("#3"); product_list[1].buy(10)
    print("#4"); product_list[2].buy(2)
    print("#5"); product_list[2].buy(1)
    print("#6"); product_list[3].buy(2)

    print("#7")
    for p in product_list:
        p.currentState()
        p.totalState()
        print()

    print("#8")
    rankTotalPrice(product_list)
