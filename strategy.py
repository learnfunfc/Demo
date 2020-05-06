
# 一般攻擊類別
class attackNormal:
    def executeAttack(self):
        print("使用一般攻擊")

#弓箭射擊列別
class attackStrategy1:
    def executeAttack(self):
        print("使用弓箭")

#流星錘攻擊類別
class attackStrategy2:
    def executeAttack(self):
        print("使用流星錘")


class Adventure:
    def __init__(self):
        self.flightStrategy = None

    def choiceStrategy(self,s):
        self.flightStrategy = s

    def attack(self):
        #如果沒有設定strategy則使用一般攻擊
        if self.flightStrategy == None:
            self.flightStrategy = attackNormal()
        self.flightStrategy.executeAttack()


#  testing code
print("遇到史萊姆>>>")
p = Adventure()
p.attack()

print("遇到吸血蝙蝠>>>")
p.choiceStrategy(attackStrategy1())
p.attack()

print("遇到大頭怪>>>")
p.choiceStrategy(attackStrategy2())
p.attack()
