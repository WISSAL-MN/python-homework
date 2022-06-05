from math import pi

val=[]
circ=[]
sur=[]
for x in range(4):
    x=input()
    val.append(int(x))
    circ.append(round(int(x)*pi*2,2))
    sur.append(round(int(x)**2*pi,2))
print (val),
print(circ),
print(sur) , 
import math
print("Donnez une liste content 4 nombres")
myList=[]
for el in range(4):
    myList.append(float(input("Donnez le nombre %d : " %  (el+1))))

print("Liste lue: " ,  myList)

diam=[]
circ=[]
area=[]
for el in myList:
    diam.append(round(el*2,2))
    circ.append(round(el *2 *  math.pi,2))
    area.append(round(el ** 2 * math.pi,2))

print("Diamètres : {0} " .format( diam))
print("Circonférences : {0} " .format( circ))
print("Surfaces : {0} " .format( area))

#deuxième méthode en utilisant les listes en compréhension
diam = [round(el *2,2)  for el in myList]
circ = [round(el *2 *  math.pi,2) for el in myList]
area = [round(el ** 2 * math.pi,2)  for el in myList]

print("Deuxième méthode de calcul:")
print("Diamètres : {0} " .format( diam))
print("Circonférences : {0} " .format( circ))
print("Surfaces : {0} " .format( area))
    
