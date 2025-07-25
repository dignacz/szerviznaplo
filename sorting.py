#szamok = [5, 2, 9, 1]
#rendezett = sorted(szamok, reverse=False)

#print(rendezett)

szervizek = [
    {"dátum": "2024-06-01", "km": "120000", "művelet": "olajcsere"},
    {"dátum": "2023-12-20", "km": "110000", "művelet": "fékolaj csere"},
    {"dátum": "2025-03-11", "km": "130000", "művelet": "szűrőcsere"},
]

#def datum_alapjan(szerviz):
    #return szerviz["dátum"]

rendezett = sorted(szervizek, key=lambda x: x["dátum"], reverse=False)

print(rendezett)