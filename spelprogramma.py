import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def minMax():
    try:
        global getal1
        global getal2
        getal1 = int(input("Wat is het minimum? "))
        getal2 = int(input("Wat is het maximum? "))
    except ValueError:
        print("Dat snap ik niet...")
        minMax()

minMax()

aantal = random.randint(getal1, getal2)

def spelprogramma(spelList):
    print(random.choice(spelList))

for i in range(aantal):
    spelprogramma(spelList)