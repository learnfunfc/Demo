class Subject:
    def __init__(self):
        self.observer_list=[]
    
    def subscript(self, obs):
        self.observer_list.append(obs)
    
    def cancel(self,obs):
        self.observer_list.remove(obs)

class Association(Subject):
    def sendQuestion(self, msg):
        for i in self.observer_list:
            i.getQuestion(msg)


class Adventure:
    def __init__(self,name):
        self.name = name

class Lancer(Adventure):
    def getQuestion(self, msg):
        print("I am %s and lancer. I got %s" %(self.name, msg))

class Bard(Adventure):
    def getQuestion(self,msg):
        if msg == "fight":
            print("I am %s and Bard. Fighting is difficult to me" %self.name)
        else:
            print("I am %s. I got %s" %(self.name, msg))

# testing code
lancer1 = Lancer("Frank")
lancer2 = Lancer("Bob")
bard1 = Bard("Jhon")
bard2 = Bard("Ken")
sub = Association()
sub.subscript(lancer1)
sub.subscript(lancer2)
sub.subscript(bard1)
sub.subscript(bard2)

sub.sendQuestion("Mission 1")
sub.sendQuestion("Mission 2")
sub.sendQuestion("fight")