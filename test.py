import json as js
def validate():
    global id
    print("LOGIN!!!")
    global f
    id=int(input("Enter ID:"))
    if id==624135:
        f=1
        print("WELCOME MASTER!!")
        return True
    else:
        return False
deck={'A.V':['STAR_CANON','BLAST_EM'],'MARIA':['BLOOD_BATH','CURSE']}
print(id)
data={}
def choose():
    if(validate()):
        global data
        c=int(input("CHOOSE A CHARACTER:\n 1.A.V \n 2.MARIA\n "))
        dex={1:"A.V",2:"MARIA"}
        print(dex[c])
        print("Your deck is:",deck[dex[c]])
        data={'ID':id,'Characters':dex[c],'DECK':deck[dex[c]]}
        data=js.dumps(data)
        with open(f"{id}.json","w") as f:
            js.dump(data,f)
    else:
        print("Invalid ID!!!")
        return False
print(data)
choose()

