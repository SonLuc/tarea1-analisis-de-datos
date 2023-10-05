import numpy as np
import statistics as st

def media(columnas, tot_col):
    medias = []
    for i in range(tot_col): medias.append(np.mean(columnas[i]))
        
    return medias
        
def mediana(columnas, tot_col):
    medianas = []
    for i in range(tot_col): medianas.append(np.median(columnas[i]))
        
    return medianas
        
def moda(columnas, tot_col):
    modas = []
    for i in range(tot_col): modas.append(st.mode(columnas[i]))
    
    return modas

def varianza(columnas, tot_col):
    varianzas = []
    for i in range(tot_col): varianzas.append(np.var(columnas[i]))
        
    return varianzas

def desviacion(columnas, tot_col):
    desviaciones = []
    for i in range(tot_col): desviaciones.append(np.std(columnas[i]))
    
    return desviaciones

def maximo_minimo(columnas, tot_col):
    maximos = []
    minimos = []
    for i in range(tot_col):
        maximos.append(np.max(columnas[i]))
        minimos.append(np.min(columnas[i]))
        
    return [maximos, minimos]
        
def rango(columnas, tot_col):
    rangos = []
    for i in range(tot_col): rangos.append(np.max(columnas[i]) - np.min(columnas[i]))
        
    return rangos