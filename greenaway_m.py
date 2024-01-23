import greenaway_o

def beolvas():
    filmek=[]
    befile=open("greenaway.txt", "r", encoding="utf-8")
    befile.readline()
    adatok=befile.readlines()
    for sor in range(0,len(adatok),1):
        tisztitott_sor=adatok[sor].strip()
        darabolt_sor=adatok[sor].split("-")
        film=greenaway_o.Film(darabolt_sor[0],darabolt_sor[1])
        filmek.append(film)

    return filmek

def harom():
    filmek=beolvas()

