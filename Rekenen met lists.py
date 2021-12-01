listOne = ['1','2','3','4','5','6','7','8','9','10']
listTwo = ['2','4','6','8','10','12','14','16','18','20']

# 2 getallen optellen
def addAndDisplayLists(getal):
    getal1 = int(listOne[getal])
    getal2 = int(listTwo[getal])
    print(getal1, "+", getal2, "=", getal1 + getal2)

print("")
print("")
print("---------")
print("Add lists")
for i in range(10):
    addAndDisplayLists(i)

# 2 getallen van elkaar aftrekken
def substractAndDisplayLists(getal):
    getal1 = int(listOne[getal])
    getal2 = int(listTwo[getal])
    print(getal1, "-", getal2, "=", getal1 - getal2)

print("")
print("")
print("---------------")
print("Substract lists")
for i in range(10):
    substractAndDisplayLists(i)

# 2 getallen keer elkaar

def multiplyAndDisplayLists(getal):
    getal1 = int(listOne[getal])
    getal2 = int(listTwo[getal])
    print(getal1, "X", getal2, "=", getal1 * getal2)

print("")
print("")
print("---------------")
print("Multiply lists")
for i in range(10):
    multiplyAndDisplayLists(i)

# 2 getallen delen
def divideAndDisplayLists(getal):
    getal1 = int(listOne[getal])
    getal2 = int(listTwo[getal])
    print(getal1, ":", getal2, "=", getal1 / getal2)

print("")
print("")
print("---------------")
print("divide lists")
for i in range(10):
    divideAndDisplayLists(i)