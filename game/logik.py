bat=[]
pt={'A':2,'B':1}
et={'A':3,'B':2,'C':1}
ph=5
eh=5
def is_alive():
    global eh
    for i in range(len(bat)):
        eh=eh-bat[i]
    """if i%2 == 1:
            eh-=bat[i]
        else:
            ph-=bat[i]"""
    if eh<=0:
        print("Villan Lost")
        return 0
    elif ph<=0:
        print("Hero Lost")
        return 0
    else:
        return 1
while 1:
    u=str(input("Enter your attack {A or B}:")).upper()
    bat.append(pt[u])
    t=is_alive()
    if t:
        print(bat)
    else:
        break

