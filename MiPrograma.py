# MiPrograma.py
import random
 
# este pograma etah tan mal exo k me changran lo oho
# -----------------------------------------------------
def sumarListaPares(lista):
    sum=0
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0:
            sum=sum+lista[i]
 
    return sum

# -----------------------------------------------------
# -----------------------------------------------------
def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print nombre + "[" + str(i) + "]=" + str(lista[i])

# -----------------------------------------------------
# -----------------------------------------------------
def crearLista():
    lista=[]
 
    i=0
    while i < 5:
        lista.append(int(random.randint(0, 5)))
        i=i+1
    return lista

# -----------------------------------------------------
# -----------------------------------------------------
A = crearLista()
imprimirLista(A,"A")
print "Suma = " + str(sumarListaPares(A))



def sumarListaImpares(lista):
#Comentario añadido por el Desarrollador A AKA BATMAN
#PD: polillas
  sum = 0
  for i in range (0, len(lista)):
    if lista[i] % 2 == 0:
      sum=sum+lista[i]
  return sum