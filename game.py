def test():
    if(show(ipchoice)):
        print("WORKS")
    else:
        print("WONKS")
ehp,php=0,0
d={}
print("Welcome to CELNEX")
ipchoice=int(input("Celnex – Heroes from all worlds battle for control and survival.\n1.A.V[The Last-Machine]\n2.MARIA[Heir of Glory]\nChoose one Character:"))
A_V={'BLAST_EM':10,'STAR_CANON':20,'HP':50}
MARIA={'CURSE':5,'BLOOD_BATH':15,'HP':65}
YOREI_SHOGUN={'CURSED_FLAME':15,'SPIRIT_DRAIN':10,'PHASE_SHIFT':0,'HP':70}
def show(c):
    print("YOUR CHARACTER CREDS:\n")
    global d
    if c==1:
        print("A.V")
        d=A_V 
        print("DECK",(k:v for k,v in d.items()if k!='HP'))
        print("HP",A_V['HP'])
    elif c==2:
        d=MARIA
        print("DECK",(k:v for k,v in d.items()if k!='HP'))
        print("HP",MARIA['HP'])
    else:
        return False
def play(d,ed):
    EHP=ed['HP']
    print("\n-------------BATTLE BEGINSSS\n----------")
    while d['HP']>0 and ed['HP']>0:
        print()
     
def start():
    show(ipchoice)
start()
