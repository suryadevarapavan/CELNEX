import json
data =""
with open('deck.json','r') as file:
    data=json.load(file)

class Character:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def info(self):
        print(f"You choice {self.name} and his HP:{self.hp}")
    def is_alive(self):
        print(self.hp > 0)
def coc():
    cd={1:"Vampire",2:"Robots"}
    c=int(input("1.Vampires\n2.Robots\nEnter choices:"))
    if c==1:
        for i in data[cd[1]]:
            print(i)
            i=dict(i)
            p1=Character(i["Name"],i["HP"])
            return p1
    elif c==2:
        for i in data[cd[2]]:
            print(i)
            i=dict(i)
            return p1
    else:
        print("Invalid choie bub!")
p2=Character("Yourei shogun",70)
while 1:
    print("Welcome to the game:\n")
    i=str(input("Press Enter to play!:\n"))
    if i == "":
        k=coc()
        k.is_alive()
        k.info()
    else:
        break

p1.info()
