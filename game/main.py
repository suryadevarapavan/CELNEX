import json
global data
data =""
with open('deck.json','r') as file:
    data=json.load(file)

class Character:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def info(self):
        print(f"You choice {self.name} and his HP:{self.hp}")

def coc():
    cd={1:"Vampire",2:"Robots"}
    c=int(input("1.Vampires\n2.Robots\nEnter choices:"))
    if c==1:
        for i in data[cd[1]]:
            print(i)
            i=dict(i)
            p1=Character(i["Name"],i["HP"])
            p1.info()
    else:
        for i in data[cd[2]]:
            print(i)
            p1=Character(i)
            p1.info()
coc()
