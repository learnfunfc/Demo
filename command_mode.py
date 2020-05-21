#定義receiver
class KitchenWorker:
    def finishOrder(self):
        pass

class BarKeep(KitchenWorker):
    def finishOrder(self):
        print("準備工作->飲料完成")

class Chef(KitchenWorker):
    def finishOrder(self):
        print("準備工作->點心完成")

# 定義order父類別
class Order:
    def __init__(self,receiver):
        self.receiver = receiver
        self.name=""
    
    # 訂單傳送給廚房人員
    def sendOrder(self):
        self.receiver.finishOrder()

    #讓其它程式知道是甚麼訂單
    def getName(self):
        return self.name

# 定義飲料訂單
class DrinkOrder(Order):
    def __init__(self,receiver):
        super().__init__(receiver)
        self.name = "drinkOrder"

# 定義點心訂單
class SnackOrder(Order):
    def __init__(self,receiver):
        super().__init__(receiver)
        self.name = "snackOrder"

# invoker 服務生
class Waitress:
    snackQty = 2
    drinkQty = 4
    orderList =[]

    # 處理訂單
    def setOrder(self,order):
        if order.name=="drinkOrder":
            if Waitress.drinkQty<0:
                print("抱歉 飲料賣完了")
            else:
                print("好的! 幫您定一份飲料")
                Waitress.drinkQty-=1
                Waitress.orderList.append(order)

        if order.name=="snackOrder":
            if Waitress.snackQty<0:
                print("抱歉 點心賣完了")
            else:
                print("好的! 幫您定一份點心")
                Waitress.snackQty-=1
                Waitress.orderList.append(order)

    # 取消訂單
    def cancelOrder(self,order):
        if order.name == "drinkOrder":
            print("好的! 幫你取消飲料訂單")
            Waitress.drinkQty+=1

        if order.name == "snackOrder":
            print("好的! 幫你取消飲料訂單")
            Waitress.snackQty+=1
            
        Waitress.orderList.remove(order)


    # 通知廚房，並且清空訂單
    def notifyBaker(self):
        for i in Waitress.orderList:
            i.sendOrder()
        Waitress.orderList=[]

# 冒險者client

snackChef = Chef()
snackOrder = SnackOrder(snackChef) # snackOrder 交給Chef處理
barkeep = BarKeep()
barOrder = DrinkOrder(barkeep) # drink 交給barkeep處理

cuteGirl = Waitress()
print("====開始點餐=====")
cuteGirl.setOrder(snackOrder)
cuteGirl.setOrder(snackOrder)
cuteGirl.setOrder(barOrder)
cuteGirl.setOrder(barOrder)
cuteGirl.cancelOrder(barOrder)
cuteGirl.notifyBaker()