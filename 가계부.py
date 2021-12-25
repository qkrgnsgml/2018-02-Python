import time
status = ["save","draw"]

class account:
    def __init__(self, name="NONE"):
        self.__id = int(time.time())
        self.__property = 0
        self.__name = name
        self.__list = []
        print self.__name,"'s account Created.."

    def __del__(self):
        print self.__name,"'s account Deleted.."

    def __str__(self):
        return self.__name+"'s account."

    def print_acc(self):
        print "| %25s | %10s | %5s | %10s | %10s |"%("Time","Bank&info","Stat","Money","Property")
        for list in self.__list:
            print "| %25s | %10s | %5s | %10d | %10d |"%(time.ctime(list[0]),list[1],list[2],list[3],list[4])

        print "\n"

    def savein(self,bank = "Def_Bank"):
        print "Select Save money."
        money = int(raw_input("How Much save : "))
        savebank = bank
        savetime = time.time()
        
        self.__property += money
        self.__list.append([savetime,savebank,status[0],money,self.__property])

    def drawout(self,info = "Drawout"):
        print "Draw Out Money."
        money = int(raw_input("How Much Draw : "))
        drawinfo = info
        drawtime = time.time()

        self.__property -= money
        self.__list.append([drawtime,drawinfo,status[1],money,self.__property])

test = 0
while 1:
    print "\n===== Account ====="
    print " 1. Create Account"
    print " 2. Print Account"
    print " 3. Save in money"
    print " 4. Draw out money"
    print " 0. EXIT"
    print "==================="
    sel = int(raw_input("Select >"))
    print ""

    if(sel == 0):
        print "EXIT Account Program."
        break
    elif(sel == 1):
        print "Create Account!"
        name = raw_input("Insert Your name >")
        test = account(name)
    elif(test == 0):
        print "You have not Account."
    elif(sel == 2):
        print test
        test.print_acc()
    elif(sel == 3):
        bank = raw_input("Where save in ?")
        test.savein(bank)
    elif(sel == 4):
        info = raw_input("Where draw out ?")
        test.drawout(info)


출처: http://maks.tistory.com/entry/Python으로-만드는-간단한-프로그램 [막장인생의 막장 스토리]
