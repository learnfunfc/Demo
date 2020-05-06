class Archer:
    def getType(self):
        print("我是弓箭手")
class Warrior:
    def getType(self):
        print("我是鬥士")

# simple factory 
class TrainingCamp:
    def trainAdventurer(self,t):
        if t=="archer":
            return Archer()
        elif t=="warrior":
            return Warrior()

camp = TrainingCamp()
a = camp.trainAdventurer("archer")
w = camp.trainAdventurer("warrior")
a.getType()
w.getType()