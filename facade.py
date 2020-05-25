class Basic:
    pass

#集氣類別
class EnergyUp(Basic):
    
    def full_up(self):
        print("集氣已滿")

# 咒語類別
class Spell(Basic):
    def say(self,word):
        print(word)

# 手勢類別
class Gesture(Basic):
    def display(self,pattern):
        print(pattern)


# 抽象技能類別
class Skill:
    def use(self):
        pass

# 雷電絕招類別
class Thunder(Skill):
    # override
    def use(self):
        energy = EnergyUp()
        energy.full_up()
        g = Gesture()
        g.display("出拳")
        print("看我的雷電絕招!")

# 暴風組絕招類別
class Storm(Skill):
    def use(self):
        g = Gesture()
        g.display("揮揮")
        s = Spell()
        s.say("天地賜我乾坤 風!")
        print("看我的暴風絕招!")

# 天蹦地裂絕招類別
class Earthquake(Skill):
    def use(self):
        energy = EnergyUp()
        energy.full_up()
        g = Gesture()
        g.display("對掌")
        s = Spell()
        s.say("天地賜我乾坤 裂!")



class Widzard:
    pass


# facade類別
# 可透過facade類別再新增其他組合密技
class Facade(Widzard):
    def storm(self):
        s = Storm()
        s.use()
    
    def thunder(self):
        t = Thunder()
        t.use()

    def earthquacke(self):
        e = Earthquake()
        e.use()

# test code

wizard = Facade()
wizard.earthquacke()
print()
wizard.storm()
print()
wizard.thunder()