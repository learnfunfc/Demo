class Adventure():
    def __init__(self,name):
        self.name = name

    def attack(self):
        pass

class Lancer(Adventure):
    def attack(self):
        print("%s使用長槍攻擊" %self.name)

# 類別修飾抽象類別
class Title():
    def __init__(self,adventure):
        self.adventure =adventure

    def attack(self):
        self.adventure.attack()

# 強壯修飾類別
class StrongTitle(Title):
    def attack(self):
        print("戰力提升100!!")
        # 呼叫Title父類別的attack方法
        super().attack()

# testing code
lancer = Lancer("Jack")
lancer.attack()

strongLancer = StrongTitle(lancer)
strongLancer.attack()