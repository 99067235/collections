import random
zak = []
zak2 = {}
hoeveel = 0
list1 = 0

colors = ["oranje", "blauw", "groen", "bruin"]


def choice():
    global i
    for i in range(hoeveel):
        new = random.choice(colors)
        if new in zak2:
            zak2[new] += 1
        else:
            zak2[new] = 1
    return zak2

def listToString(list1):
    return str(list1).replace('[', '').replace(']', '')
    
def snapNiet():
    print("Sorry dat snap ik niet...")
    print("")

def hoeveelstuks():
    global hoeveel
    try:
        hoeveel = int(input("Hoeveel M&M's wil je in de zak van Sinterklaas? "))
        if hoeveel >= 0:
            print(toevoegen(hoeveel))
            choice()
            kleur = int(input("Hoeveel kleuren moeten er aan de zak toegevoegd worden? "))
            if kleur >= 0:
                listToString(list1)
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