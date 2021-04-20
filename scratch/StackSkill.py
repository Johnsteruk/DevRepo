#!/usr/bin/env python3

#kingsName = input("Please enter your name, your majesty : ")

#numberOfJewels = input("Enter the number of jewels: ")
#priceOfJewels = input("Enter the price of each jewel :")

#totalCosts = int(numberOfJewels) * int(priceOfJewels)

#print(f"The total costs of price of these will be : {totalCosts}")

musketeerNames = ['Porthos','Athos', 'Aramis']
musketeerAges = [55,34,67]
musketeerNames.insert(0,"D'artagnan")
musketeerAges.append(16)
tempVariable = musketeerNames.pop(0)
musketeerNames.append(tempVariable)

print(musketeerNames)
print(musketeerAges)
print(f"Total number of musketeers : {str(len(musketeerNames))}")

#dudeToKill = input("Enter a a number from 1 to 4 to kill as scapegoat : ")
#dudeToKill = int(dudeToKill) -1
#print(f"You have chosen to kill {musketeerNames[dudeToKill]} aged {musketeerAges[dudeToKill]}")

dictVar = {}
dictVar['pi'] = 3.14
dictVar[25] = 'Square of negative 5'
dictVar['John'] = 'Some dudes name'
print(dictVar.keys())
print(dictVar.values())

def get_key(valueToFind, inputDict):
    for k, v in inputDict.items():  
        if v == valueToFind:
            return k

#print(dictVar[list(dictVar.values()).index(3.14)])
#print(get_key('Some dudes name', dictVar))

inputKeyToDelete = input(f'Enter the key of the pair you want to delete : {dictVar.keys()} ')

if inputKeyToDelete in dictVar:
    dictVar.pop(inputKeyToDelete)
    print(f'{inputKeyToDelete} has been removed. Look - {dictVar.keys()}')