"""
1. feladat
Olvassa be és tárolja el a beosztas.txt állományban talált adatokat, és annak
felhasználásával oldja meg a következő feladatokat! 
"""
beosztas={}
beosztasok=[]
seged_lista=[]

with open("beosztas.txt","r",encoding="UTF-8")as fm1:
    for sor in fm1:
        seged_lista.append(sor.strip())
        if len(seged_lista)==4:
            beosztas["tanar"]=seged_lista[0]
            beosztas["tantargy"]=seged_lista[1]
            beosztas["osztaly"]=seged_lista[2]
            beosztas["oraszam"]=int(seged_lista[3])
            beosztasok.append(beosztas)
            seged_lista=[]
            beosztas={}


#print(beosztasok)

"""
2. feladat
Hány bejegyzés található az állományban? Az eredményt írassa ki a képernyőre! 
2. feladat
A fájlban 329 bejegyzés van.
"""
print("2. feladat")
print(f"2. feladat A fájlban {len(beosztasok)} bejegyzés van.")

"""
3. feladat
Mennyi a heti ossz oraszam a susuba?
3. feladat
Az iskolában a heti összóraszám: 1016
"""
def osszegzes(bok):
    osszeg=0
    for elem in bok:
        osszeg+=elem["oraszam"]
    return osszeg


print("3. feladat")
print(f"Az iskolában a heti összóraszám:  {osszegzes(beosztasok)}")