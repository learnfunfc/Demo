class Archer:
    def shot(self):
        print("弓箭發射了!")

class Wizard:
    def fireball(self):
        print("投擲火球")

# 只需要寫Adpater類別，而不去動到archer和 wizard類別
class Adapter(Wizard):
    # 傳入archer 物件
    def __init__(self,archer):
        self.archer = archer
    # override
    def fireball(self):
        print("射出有火的箭")
        


# 測試

new_archer = Adapter(Archer())
new_archer.fireball()