import time
import random
first=1
money = 5
list = ["face"]
intro=["Hello!","Welcome to Callum's RPG!","A place where monsters reign,","but where heroes dwell and grow.","You my friend,","shall have to defeat the evil that lurks across the land.","The mighty and powerful,","Rowan.","It shall be difficult,","but I sense something special about you.","Go ahead and start your journey,","but remember to ask for help if you have no idea what to do."]
Bobo_intro=["???: *grumble* Fine, come on in.", "???: Just don't ask me for money for your little club or somthing.","???: And we don't have candy either.", "???: Oh! Sorry, I didn't know that an adventurer would come here!","Bobo: My name is Bobo, the humble owner of this shop.","Bobo: We have many things for people like you.","Bobo: swords, shields, and more!","Bobo: Just make sure you have enough money, and anything is yours."]
Bobo=["Bobo: Hello there!","Bobo: No monsters here, eh?","Bobo: Welcome to Bobo's Armory!"]
sword_index=["dagger", "broadsword", "short-sword", "scimitar", "enchanted-sword"]
shield_index=["large-shield", "circle-shield", "kite-shield", "spiked-shield", "golem-shield"]
for s in intro:
    print s
    time.sleep(2)
class Game:
    def __init__(self, HP, ATTK):
        self.HP = HP
        self.ATTK = ATTK
player = Game("20", "5")
exp=110
level=1
level_req=110
class Sword:
    def __init__(self,ATK,SPD):
        self.ATK = ATK
        self.SPD = SPD
dagger = Sword("3","5")
def level_up():
    global exp
    global level
    global level_req
    if exp == level_req or exp > level_req:
        player.ATK=int(player.ATK) +1
        player.HP=int(player.HP) +2
        level=level+1
        exp = exp - level_req
        level_req = level * 100 + level * 10
def NPC_text():
    global list
    print list[int((random.uniform(0,3)))]
def Sword_Select(swordex):
    print "{} ATK".format(swordex.ATK)
    print "{} SPD".format(swordex.SPD)
    print "Do u want to dab or play Basketball?"
while True:
    place = raw_input("Where shall you go? ")
    if place == "shop":
        if money > 0:
            if first == 1:
                for i in Bobo_intro:
                    print i
                    time.sleep(1.8)
                first=0
            list=Bobo
            NPC_text()
            gear_type = raw_input ("What type of stuff do you want? ")
            if gear_type == "swords":
                print sword_index
                sword = raw_input("What sword do you want? ")
                if sword == "dagger":
                    Sword_Select(dagger)
            elif gear_type == "shields":
                print shield_index
                shield = raw_input("What shield do you want? ")
                for x in shield_index:
                    if shield == x:
                        print shield
        else:
            print "You can type in shop."
