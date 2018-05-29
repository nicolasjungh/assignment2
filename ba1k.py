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

print(computingfrequencies(input("Geben Sie bitte hier den DNA-Code ein: "), int(input("Geben Sie bitte hier die Länge des k-mers ein: "))))