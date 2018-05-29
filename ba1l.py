liste1 = list(input("Bitte DNA-Seqenz eingeben: "))
liste2 = []
x = 1
y = len(liste1)-1
z = 0
for i in range (0,y+1):
 if liste1[len(liste1)-x] == "A":
    z = z+(0*4**(x-1))
 if liste1[len(liste1)-x] == "C":
    z = z+(1*4**(x-1))
 if liste1[len(liste1)-x] == "G":
     z = z + (2*4**(x-1))
 if liste1[len(liste1) -x] == "T":
    z = z+(3*4**(x-1))
 x = x+1
 y = y-1

print(z)


