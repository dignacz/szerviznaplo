with open("pelda.txt", "w", encoding="utf-8") as f:
    f.write("Ez egy próba: á, é, ü, 😀")

with open("pelda.txt", "r", encoding="utf-8") as f:
    print(f.read())
