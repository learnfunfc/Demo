
# 定義上衣裝備類別
class Clothes:
    def __init__(self):
        self.defence=0
    
    def display(self):
        classType = str( type(self)).split('.')
        classType=classType[1][:-2]
        print( classType +"抵禦能力為:"+ str( self.defence) )

    def setDef(self, level):
        self.defence = level

# 盔甲上衣 for 鬥士
class Armor(Clothes):
    pass

#皮甲上衣for 弓箭手
class Leather(Clothes):
    pass



# 定義武器備類別
class Weapon:
    def __init__(self):
        self.attack=0
        self.range=0

    def setAttack(self,p):
        self.attack = p

    def setRange(self,r):
        self.range = r
    
    def display(self):
        classType = str( type(self)).split('.')
        classType=classType[1][:-2]
        print( classType +"攻擊能力為:"+ str( self.attack) )
        print( classType +"攻擊範圍為:"+ str( self.range) )

#定義弓類別
class Bow(Weapon):
    pass

#定義長劍類別
class LongSword(Weapon):
    pass



# 定義弓箭手裝備工廠
class ArcherEquip():
    def createBow(self):
        b = Bow()
        b.setAttack(5)
        b.setRange(10)
        return b
    
    def createLeather(self):
        l = Leather()
        l.setDef(5)
        return l

#定義武士裝備工廠
class WarriorEquip():
    def createLongSword(self):
        s = LongSword()
        s.setRange(5)
        s.setAttack(10)
        return s

    def createArmor(self):
        a = Armor()
        a.setDef(10)
        return a


#定義冒險者類別
class Adventure:
    def setWeapon(self, w):
        self.weapon = w

    def setClothe(self,c):
        self.cloth = c

    def display(self):
        classType = str( type(self)).split('.')
        classType=classType[1][:-2]
        print("裝備:")
        self.weapon.display();
        self.cloth.display();
        

class Archer(Adventure):
    def getType(self):
        print("我是弓箭手")


class Warrior(Adventure):
    def getType(self):
        print("我是鬥士")


class ArcherTrainingCamp:
    def training(self):
        factory = ArcherEquip()
        archer = Archer()
        archer.setWeapon(factory.createBow())
        archer.setClothe(factory.createLeather())
        return archer

class WarriorTrainCamp:  
    def training(self):
        factory = WarriorEquip()
        warrior = Warrior()

        warrior.setWeapon(factory.createLongSword())
        warrior.setClothe(factory.createArmor())
        return warrior



# main test code
w = WarriorTrainCamp()
p1 = w.training()
p1.getType()
p1.display()