SymbolToNumber = {'A':0, 'C':1, 'G':2, 'T':3}
NumberToSymbol = {0:'A', 1:'C', 2:'G', 3:'T'}

def Numbertopattern(zahl,k):
    if k == 1:
        return NumberToSymbol[zahl]
    x = zahl // 4
    y = zahl % 4
    prefixPattern = Numbertopattern(x, k - 1)
    return prefixPattern + NumberToSymbol[y]




def patterntonumber(DNASequenz):
 liste2 = []
 x = 1
 y = len(DNASequenz)-1
 z = 0
 for i in range (0,y+1):
  if DNASequenz[len(DNASequenz)-x] == "A":
    z = z+(0*4**(x-1))
  if DNASequenz[len(DNASequenz)-x] == "C":
    z = z+(1*4**(x-1))
  if DNASequenz[len(DNASequenz)-x] == "G":
     z = z + (2*4**(x-1))
  if DNASequenz[len(DNASequenz) -x] == "T":
    z = z+(3*4**(x-1))
  x = x+1
  y = y-1
  return(z)

def computingfrequencies(DNASequenz, k):
     h = -1 + 4 ** k
     for i in range(0, h):
         frequencyarray = [0]*(4 ** k)
     for i in range(0, (len(DNASequenz) - k + 1)):
         pattern = DNASequenz[i:i + k]
         j = int(patterntonumber(pattern))
         w = frequencyarray[j]
         w = w + 1
         frequencyarray[j] = w

     return (frequencyarray)

DNASequenz=input("Geben Sie bitte die DNA-Sequenz ein: ")
k=int(input("Geben Sie bitte die Länge des k-mers ein: "))
frequencyarray=computingfrequencies(DNASequenz,k)

frequentPatterns = []
COUNT = [0] * len(DNASequenz)
maxwords= max(frequencyarray)
for i in range(0,4**k):
   if frequencyarray[i]==maxwords:
       Pattern= Numbertopattern(i,k)
       frequentPatterns.append(Pattern)



print(frequentPatterns)