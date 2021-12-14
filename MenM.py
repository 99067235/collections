import random
zak = []
zak2 = {}
soortCheck = 0

colors = ["oranje", "blauw", "groen", "bruin"]



    
def diction(kleur):
    for i in range(hoeveel):
        new = random.choice(colors)
        if new in zak2:
            zak2[new] += 1
        else:
            zak2[new] = 1
    return zak2


def snapNiet():
    print("Sorry dat snap ik niet...")
    print("")

def hoeveelstuks():
    global hoeveel
    try:
        hoeveel = int(input("Hoeveel M&M's wil je in je zakje? "))
        if hoeveel >= 0:
            print(toevoegen(hoeveel))
            kleur = int(input("Hoeveel kleuren moeten er aan de zak toegevoegd worden? "))
            if kleur >= 0:
                print(diction(kleur))
                sorteren(soortCheck)
            else:
                snapNiet()
        else:
            snapNiet()
            hoeveelstuks()
    except ValueError:
        snapNiet()
        hoeveelstuks()

def toevoegen(aantal):
    for i in range(aantal):
        new = random.choice(colors)
        zak.append(new)
    return zak

hoeveelstuks()