import random
def general(alsohatar, felsohatar):
    print("II/a.")
    print("\t", end=" ")
    szamok_listaja=[]
    if felsohatar<alsohatar:
        atmenet=alsohatar
        alsohatar=felsohatar
        felsohatar=atmenet
    db=0
    while(db<15):
        vszam=random.randint(alsohatar,felsohatar)
        szamok_listaja.append(vszam)
        print(f"{vszam}%",end=" ")
        db+=1
    vszam=random.randint(alsohatar,felsohatar)
    print(f"{vszam}")
    return szamok_listaja

def legkisebb(szamok_listaja):
    minErtek=szamok_listaja[0]
    minHely=0
    for index in range(0,len(szamok_listaja),1):
        if szamok_listaja[index]<minErtek:
            minErtek=szamok_listaja[index]
            minHely=index
    print("II/b.")
    print(f"A legkisebb elem:{minErtek}.")
    kiFajl=open("legkisebb.txt","w", encoding="utf-8")
    print("II/b.", file=kiFajl)
    print(f"\tA legkisebb elem:{minErtek}.", file=kiFajl)

    #


def ketto():
    szamok_listaja=general(100,200)
    legkisebb(szamok_listaja)