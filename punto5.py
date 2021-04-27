abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abcsm3 = []
for a in range(6):
    if a%3 != 0:
        abcsm3.append(abc[a])
print(abcsm3)
