import random
zak = []
hoeveel = 0

colors = ["oranje", "blauw", "groen", "bruin"]

def snapNiet():
    print("Sorry dat snap ik niet...")
    print("")

def hoeveelstuks():
    global hoeveel
    hoeveel = int(input("Hoeveel M&M's wil je in je zakje? "))
    if hoeveel >= 0:
        toevoegen()
    else:
        snapNiet()
        hoeveelstuks()

def toevoegen():
    for i in range(hoeveel):
        new = random.choice(colors)
        zak.append(new)
    return zak

hoeveelstuks()