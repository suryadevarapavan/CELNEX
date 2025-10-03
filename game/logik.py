bat=[]
pt={'A':2,'B':1}
et={'A':3,'B':2,'C':1}
ph=5
eh=5
hc=0
ec=0
def is_alive():
    global eh
    for i in range(len(bat)):
        eh-=bat[i]
        if i%2 == 1:
            print(bat[i])
            #eh-=bat[i]
        else:
            print(bat[i])
            #ph-=bat[i]
    if eh<=0:
        print("Villan Lost")
        return 0
    elif ph<=0:
        print("Hero Lost")
        return 0
    else:
        bat.clear()
        return 1
while 1:
    u=str(input("Enter your attack {A or B}:")).upper()
    if hc%2!=0 and u=='A':
        u='B'
    bat.append(pt[u])
    hc+=1
    if ec%3==0:
        bat.append(pt["A"])
    elif ec%3==1:
        bat.append(pt["B"])
    elif ec%3==2:
        bat.append(pt["c"])
    ec+=1
    t=is_alive()
    if t:
        print(bat)
    else:
        break

