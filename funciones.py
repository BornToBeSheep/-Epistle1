"""def inicializar-v 
"""

from typing import BinaryIO


def SumaDec (decimales):
    """
    Esta funcion retorna la suma total de todos los elementos de una lista
    """
    suma = 0
    for i in range (len(decimales)):
        suma += decimales[i]
    return suma


def descomponer (decimal):
    """
    Esta funcion descompone un numero decimal para encontrar sus restos
    """
    i=0
    binario= [0,0,0,0,0,0,0,0]
    while decimal != 0:
        binario[i] = decimal % 2
        decimal = decimal // 2
        i += 1 
    return binario 

def bssbcs(binario):
    """
        Esta funcion convierte un numero binario en su representacion decimal en BCS
    """
    BCS=0
    for i in range (0,7,1):
        if binario[i] == 1: 
            BCS += 2**i
    return BCS

def bssca1(binario): 
    Ca1=0
    if binario[7] == 1:
        for i in range (0,7,1):
            if binario[i] == 0:
                Ca1 += 2**i
    return Ca1
    """
        Esta funcion convierte un numero binario
        en su representacion decimal en Ca1
    
    Ca1=0
    if binario[7] == 1:
        for i in range (0,7,1):
            if binario[i] == 1:
                binario[i]= 0
            else:
                binario[i]= 1
    Ca1= bssbcs(binario)
    return Ca1
    """
    
def bssca2(binario):
    Ca2=0
    i= 0
    if binario[7] == 1:
        while binario[i] != 1:
            i+= 1
        for x in range (i,7,1):
            if binario[x] == 0:
                Ca2 += 2**x
    return Ca2
    """
        Esta funcion convierte un numero binario en su representacion decimal en Ca2
    
    Ca2=0
    i= 0
    if binario[7] == 1:
        while binario[i] != 1:
            i+= 1
        i= i+1
        for x in range (i,7,1):
            if binario[x] == 1:
                binario[x] = 0
            else:
                binario[x] = 1
        Ca2 = bssbcs(binario)
        return Ca2
    """
    

def bssex (binario):
    Ex = 0
    i = 0
    bin = 0
    if binario[7] == 1:
        for i in range (i, 7, 1):
            if binario[i] == 1:
                Ex += 2**i
        return Ex
    else:
        print (i)
        for i in range (i, 7, 1):
            if binario[i] == 1:
                bin += 2**i
        Ex = 2**7 - bin
        return Ex 