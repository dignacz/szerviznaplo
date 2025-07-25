import json
import os
from datetime import datetime

fajlnev = "szervizadat.json"

if os.path.exists(fajlnev):
    with open(fajlnev, "r", encoding="utf-8") as f:
        szervizek = json.load(f)
else:
    szervizek = []

#FÜGGVÉNYEK

def ujbejegyzes(szervizek):
    try:
        datum = input("Add meg a dátumot (pl. 2025-05-27): ")
        datetime.strptime(datum, "%Y-%m-%d")
        km = int(input("Kilométeróra állása: "))
        muvelet = input("Mit csináltál? (pl. olajcsere): ")

        szervizek.append({
            "dátum": datum,
            "km": km,
            "művelet": muvelet
        })
    except ValueError:
        print("Hibás adatbevitel! Próbáld újra.")

def listazas(szervizek):
    for szerviz in szervizek:
        print(f"{szerviz["dátum"]} ; {szerviz["km"]} ; {szerviz["művelet"]}")

def kereses(szervizek):
    kulcsszo = input("Mit keresel a szerviznaplóban? (pl. olajcsere)")
    talalatok = [s for s in szervizek if kulcsszo.lower() in s["művelet"].lower()]

    print("\nTalált bejegyzések:")
    for sz in talalatok:
        print(f"{sz['dátum']} | {sz['km']} km | {sz['művelet']}")

def rendez(szervizek, kulcs, csokkeno=False):
    if kulcs == "dátum":
        return sorted(szervizek, key=lambda x: x["dátum"], reverse=csokkeno)
    elif kulcs == "km":
        return sorted(szervizek, key=lambda x: x["km"], reverse=csokkeno)
    


#----MENÜ----

while True:
    print("\n--- Szerviz napló ---")
    print("\n1. Új bejegyzés\n2. Listázás\n3. Keresés\n4. Kilépés")
    print("\ndátum-növ: dátum rendezés növekvő") #ez már kész
    print("\ndátum-csök: dátum rendezés csökkenő")
    print("\nkm-növ: km óra rendezés növekvő")
    print("\nkm-csök: km óra rendezés csökkenő")
    valasz = input("Válassz műveletet (1-4, vagy rendezés): ")

    #Új bejegyzés
    if valasz == "1":
        ujbejegyzes(szervizek)
    #Listázás
    elif valasz == "2":
        listazas(szervizek)
    #Keresés
    elif valasz =="3":
        kereses(szervizek)
    #Rendezés dátum szerint
    elif valasz == "dátum-növ":
        listazas(rendez(szervizek, "dátum", csokkeno=False))
    elif valasz == "dátum-csök":
        listazas(rendez(szervizek, "dátum", csokkeno=True))
    elif valasz == "km-növ":
        listazas(rendez(szervizek, "km", csokkeno=False))
    elif valasz == "km-csök":
        listazas(rendez(szervizek, "km", csokkeno=True))

    #Kilépés
    elif valasz == "4":
        break

    #Ismeretlen
    else:
        print("Ismeretlen opció")



#Mentés JSON fájlba
with open(fajlnev, "w", encoding="utf-8") as f:
    json.dump(szervizek, f, indent=2, ensure_ascii=False)

print("\n--- Szerviznapló elmentve ---")