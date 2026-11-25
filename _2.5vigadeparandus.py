print("Aastaaeg")
kuu = int(input("Sisesta kuu number (1-12) => "))

# PARANDUS: and asemel or, sest kuu ei saa olla korraga alla 1 ja üle 12
if kuu < 1 or kuu > 12:
    print("Vigane kuu")

# PARANDUS: := asemel ==, sest kontrollime kuu väärtust
elif kuu == 12 or kuu <= 2:
    print("Talv")

elif 3 <= kuu <= 5:
    print("Kevad")

elif 6 <= kuu <= 8:
    print("Suvi")

elif 9 <= kuu <= 11:
    print("Sügis")

print()

print("Kiiruse kontroll")
lubatud = int(input("Sisesta lubatud kiirus (km/h) => "))

# PARANDUS: lisasin int(), sest muidu ei saa arvudega lahutada
kiirus = int(input("Sisesta tegelik kiirus (km/h) => "))

yletus = kiirus - lubatud

if yletus <= 0:
    print("Kiirust ei ületatud")

# PARANDUS: tingimused panin suuremast väiksemani
elif yletus > 40:
    print("Juhiluba võetakse ära")

elif yletus > 20:
    print("Trahv")

else:
    print("Hoiatus")

print()

print("Taksosõit")
km = float(input("Sisesta sõidu pikkus (km) => "))
oo = input("Kas sõit on öösel (jah/ei)? => ")

hind = 3 + km + 0.8

# PARANDUS: and asemel or, sest kasutaja võib kirjutada jah või JAH
if oo == "jah" or oo == "JAH":
    hind = hind * 1.2

print("Sõidu hind:", round(hind, 2), "€")


# Lisaülesanne:
print()
print("Vali programm")
print("1 - Aastaaeg")
print("2 - Kiiruse kontroll")
print("3 - Taksosõit")

# PARANDUS: parandasin kirjavea Siseta -> Sisesta
programm = int(input("Sisesta programmi number (1-3) => "))

# PARANDUS: kasutasin ==, sest kontrollime täpset programmi numbrit
if programm == 1:
    print("Aastaaeg")
    kuu = int(input("Sisesta kuu number (1-12) => "))

    if kuu < 1 or kuu > 12:
        print("Vigane kuu")
    elif kuu == 12 or kuu <= 2:
        print("Talv")
    elif 3 <= kuu <= 5:
        print("Kevad")
    elif 6 <= kuu <= 8:
        print("Suvi")
    elif 9 <= kuu <= 11:
        print("Sügis")

elif programm == 2:
    print("Kiiruse kontroll")
    lubatud = int(input("Sisesta lubatud kiirus (km/h) => "))
    kiirus = int(input("Sisesta tegelik kiirus (km/h) => "))

    yletus = kiirus - lubatud

    if yletus <= 0:
        print("Kiirust ei ületatud")
    elif yletus > 40:
        print("Juhiluba võetakse ära")
    elif yletus > 20:
        print("Trahv")
    else:
        print("Hoiatus")

elif programm == 3:
    print("Taksosõit")
    km = float(input("Sisesta sõidu pikkus (km) => "))
    oo = input("Kas sõit on öösel (jah/ei)? => ")

    hind = 3 + km + 0.8

    if oo == "jah" or oo == "JAH":
        hind = hind * 1.2

    print("Sõidu hind:", round(hind, 2), "€")

# PARANDUS: lisasin else, et vale programmi numbri korral tuleks veateade
else:
    print("Vigane programmi number")