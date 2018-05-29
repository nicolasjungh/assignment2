SymbolToNumber = {'A':0, 'C':1, 'G':2, 'T':3}
NumberToSymbol = {0:'A', 1:'C', 2:'G', 3:'T'}

def Numbertopattern(zahl,k):
    if k == 1:
        return NumberToSymbol[zahl]
    x = zahl // 4
    y = zahl % 4
    prefixPattern = Numbertopattern(x, k - 1)
    return prefixPattern + NumberToSymbol[y]
print(Numbertopattern(int(input("Geben Sie bitte die Zahl hier ein: ")),(int(input("Geben Sie bitte die Länge des DNA-Codes hier ein: ")))))


