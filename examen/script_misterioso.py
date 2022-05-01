muestras_2 = []

def obtener_media(lista):
    sumatoria = 0

    for valor in lista:
        sumatoria += valor
    longitud = len(lista)

    return sumatoria / longitud

obtener_media(muestras_2)