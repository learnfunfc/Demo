'''
class WarriorPlain:
    def __init__(self):
        self.hp = 100
    
    # 治療的方法
    def heal(self,heal):
        # 無法戰鬥的時候不能接受治療
        if(hp==0): 
            hp = 0
        else:
            self.hp += heal
        if hp>100:
            hp = 100

    #受到傷害減少hp
    def getDamage(self,damage):
        self.hp -= damage
        if hp < 0:
            hp = 0

    # 未使用狀態模式
    def move(self):
        if hp == 0:
            print("無法戰鬥")
        if hp > 70:
            print("一般狀態")
        elif hp < 30:
            print("背水一戰")
        else:
            print("狂怒狀態")

'''

''' 使用狀態模式重構'''
class NormalState:
    def content(self, warrior):
        if warrior.getHP() > 70:
            print("一般狀態")
        # 如果沒有大於70 則將warrior設為 FuryState狂怒狀態
        else:
            warrior.setState( FuryState())
            print("FuryState切換")
            warrior.move()

# 狂怒狀態     
class FuryState:
    def content(self, warrior):
        # 當狂怒狀態獲得>70血量時，將狀態切換成一般狀態
        if warrior.getHP()> 70:
            warrior.setState(NormalState())
            warrior.move()
        # 當狂怒狀態獲得<=30血量時，將狀態切換成背水一戰狀態
        elif warrior.getHP() <= 30:
            warrior.setState(DesperateState())
            print("DesperateState切換")
            warrior.move()
        else:
            print("目前血量為:{} 處於狂怒狀態".format(warrior.getHP()))


# 背水一戰狀態
class DesperateState:
    def content(self, warrior):
        if warrior.getHP() == 0:
            warrior.setState(UnableState())
            warrior.move()
        elif warrior.getHP()>30:
            warrior.setState(FuryState())
            print("FuryState切換")
            warrior.move()
        else:
            print("目前血量為:{} 處於背水一戰狀態".format(warrior.hp))


# 無能力狀態
class UnableState:
    def content(self,warrior):
        print("目前血量為:{} 處於無法戰鬥狀態".format(warrior.hp))



# 戰士類別
class Warrior:
    # 初始化為一般狀態
    def __init__(self):
        self.hp = 100
        self.state = NormalState()  

    # 治療的方法
    def heal(self,heal):
        # 無法戰鬥的時候不能接受治療
        if(self.hp==0): 
            self.hp = 0
        else:
            self.hp += heal
        if self.hp>100:
            self.hp = 100

    #受到傷害減少hp
    def getDamage(self,damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
       
    # 執行狀態的方法
    def move(self):
        self.state.content(self)

    # 設定狀態
    def setState(self,state):
        self.state = state

    # 取得hp
    def getHP(self):
        return self.hp


# to test code
w = Warrior()
w.move()
print("--------受到傷害 70%-------------")
w.getDamage(30)
w.move()
print("--------受到傷害 損傷40%---------")
w.getDamage(40)
w.move()
print("--------治癒療傷 恢復70%---------")
w.heal(70)
w.move()
