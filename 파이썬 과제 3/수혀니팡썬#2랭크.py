class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        self.totstock=0
        self.totprice=0


    def buy(self,sell=1):
        print("{0}의 총 판매가격은 {1} 구매하겠습니까?(Y/N)".format(self.name,self.price),end="")
        answer=input()
        if answer=="Y":
            if (self.stock<sell):
                print("{0}의 판매할 재고 수량이 없음".format(self.name))
            else:
                print("{0}제품 {1} 개 총 {2}에 판매하였습니다.".format(self.name,sell,self.price*sell))
                self.totstock=self.totstock+sell
                self.stock-=sell
                self.totprice += self.price*sell
        elif answer=="N":
            pass
            
    def currentState(self):
        print("제품명:{0} 단가{1} 재고:{2}".format(self.name,self.price,self.stock))
        
        
    def totalState(self):
        print("제품명:{0} 총 판매 수량:{1} 총 판매 금액:{2}".format(self.name,self.totstock,self.totprice))

def rankTotalPrice(*pro_l):
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


if __name__=="__main__":
    product_list=[ Product(name="연필",price=1000,stock=10)
                   ,Product(name="샤프",price=3000,stock=5)
                   ,Product(name="공책",price=2000,stock=5)
                   ,Product(name="볼펜",price=2000,stock=5)]
    
    print("#1"); product_list[0].buy()
    print("#2"); product_list[0].buy()
    print("#3"); product_list[1].buy(10)
    print("#4"); product_list[2].buy(2)
    print("#5"); product_list[2].buy(1)
    print("#6"); product_list[3].buy(2)
    
    print("#1")
    for p in product_list:
        p.currentState()
        p.totalState()
        print("")
    print("#8")
    rankTotalPrice(product_list)
