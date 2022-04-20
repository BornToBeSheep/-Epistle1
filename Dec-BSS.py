"""import funciones as f

f.inicialziar-v (vector)"""
"""import funciones as f
decimales= [1,2,3,4,5,10]
print(f.SumaDec (decimales))"""


import funciones as f

Dec = int(input("Ingrese el valor a convertir: "))
if Dec < 256 and Dec >= 0:
    binario = f.descomponer(Dec)
else: 
    print("El numero ingresado esta por fuera del rango de analisis")  
print(binario)


#    -----------------------------------------


"""
    Ahora convertiremos el BSS resultante en BCS
"""
BCS = f.bssbcs(binario)
if binario[7] == 0:
    print("El numero es positivo en BCS")
    print ("Representa el:" + " " + str(BCS))
else: 
    print("El numero es negativo en BCS")
    print("Representa el:" + " " + str(-BCS))


#   -----------------------------------------     


"""
    Ahora convertiremos el BSS resultante en Ca1
"""
Ca1= f.bssca1(binario)
if  binario[7] == 0:
    print("El numero es positivo en Ca1")
    print ("Representa el:" + " " + str(Ca1))
else: 
    print("El numero es negativo en Ca1")
    print("Representa el:" + " " + str(-Ca1))
print(binario)


#   -----------------------------------------  


"""
    Ahora convertiremos el BSS resultante en Ca2
"""
Ca2 = f.bssca2 (binario)
if  binario[7] == 0:
    print("El numero es positivo en Ca2")
    print ("Representa el:" + " " + str(Ca2))
else: 
    print("El numero es negativo en Ca2")
    print("Representa el:" + " " + str(-Ca2))
print(binario)


#   -----------------------------------------  


"""
    Ahora convertiremos el BSS resultante en Ex
"""
Ex = f.bssex (binario)
if  binario[7] == 1:
    print("El numero es positivo en Ex")
    print ("Representa el:" + " " + str(Ex))
else: 
    print("El numero es negativo en Ex")
    print("Representa el:" + " " + str(-Ex))
print(binario)