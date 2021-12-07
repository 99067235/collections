import random
zak = []
zak2 = {}
hoeveel = 0

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
            int(input("Hoeveel M&M's wil je in je zakje? "))
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