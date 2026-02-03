# Goblin Assault
# Norse Music - Nordic Versecraft - Bloodr ok Eldr  --  Blood and Fire 

#BEGDEF
"Purpose: Stage 1 Enemy Prototype"

class GoblinProto:
    def __init__(self,name,type,hp,mp,defence,attack):
        self.goblin_Name = name
        self.goblinType = type
        self.goblinHP = hp
        self.goblinMP = mp
        self.goblinDEF = defence
        self.goblinATT = attack
        
    def display_info(self):
        print("The enemies name is: " + self.goblin_Name)
        print("The enemies type is: " + self.goblinType)
        print("The enemies current HP: " + str(self.goblinHP))
        print("The enemies current MP: " + str(self.goblinMP))
        print("The enemies Defence: " + str(self.goblinDEF))
        print("The enemies Attack: " + str(self.goblinATT))
    
# Goblin Chief Prototype
class ChiefGoblin(GoblinProto):
    def __init__(self,name_in,spec_ab1,spec_ab2):
        self.name = name_in
        self.shoe_throw = spec_ab1
        self.fake_leg = spec_ab2
    def display_info(self):
        print("The Goblin Chief's name is: " + self.name)
        print("The Goblin Chief's type is: " + self.goblinType)
        print("The Goblin Chief uses " + self.shoe_throw)
        print("The Goblin Chief uses " + self.fake_leg)

    def isBoss(self):
            if self.goblinType == "Chief":
                return print(True)
            else:
                return print(False)
             
    def damage(self,heroDEF):
        hit = self.goblinATT * ((100 - self.heroDEF)/ 100)

class Hero:
    def __init__(self,name,type,hp,mp,defence,attack):
         self.name = name
         self.type = type
         self.hp = hp
         self.mp = mp
         self.heroDEF = defence
         self.heroATT = attack
    
    def display_info(self):
         print(self.name)
         print(self.type)
         print(int(self.hp))
         print(int(self.mp))
         print(int(self.heroDEF))
         print(int(self.heroATT))

    def damage(self,goblinDef):
         enemy = GoblinProto(name,type,hp,mp,defence,attack)
         hit = self.heroATT * ((100 - self.goblinDef) / 100)

class Thief:
    def __init__(self,spec_ab1,spec_ab2):
    Hero.__init__(self,name,type,hp,mp,defence,attack):
    self.steal = spec_ab1
    self.stab = spec_ab2

class Warrior:
    def __init__(self,spec_ab1,spec_ab2):
    Hero.__init__(self,name,type,hp,mp,defence,attack):
    self.roar = spec_ab1 
    self.rage = spec_ab2

#ENDDEF

farmGoblin = GoblinProto("Lucas","Infantry",10,0,5,1)
teaCupGoblin = GoblinProto("Rio","Teacup Collector",15,1,6,2)
wozNiak = ChiefGoblin("Wozniak","Chief",20,0,7,5)

farmGoblin.display_info()
farmGoblin.isBoss()

farmGoblin.damage()

heroZero = Hero("Expendable","Hero",35,20,10,10)
heroZero.display_info
heroZero.damage()

while heroZero.hp != 0:
    print("Attacked! Encountered one enemy!")
    print("Pre-emptive strike!")
    print("You hit the enemy for " + str(heroZero.damage(5)) + " points of damage.")
    
    
