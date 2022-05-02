import re
#1
#a)
import re
texto = "xsabc9cabcb3sabc9"
patron = "bc9"
print(re.search(patron, texto))
#print(re.search(bc9,xsabc9cabcb3sabc9))

#<re.Match object; span=(3, 6), match='bc9'>

import re
texto = "xsabc9cabcb3sabc9"
patron = "bc9"
print(re.findall(patron, texto))
#print(re.findall(bc9,xsabc9cabcb3sabc9))

#['bc9', 'bc9']

import re
def cuantas_veces(string):
    resultado = re.findall("bc9", string)
    return len(resultado)

#b)
string = "aa([^c]*?)gg"  #aa literal | grupo de todo lo que no tenga c + cualquier caracter que se repita 0 o mas veces| gg literal
patron = "ttaatatggttaacatgg"

def obtener_substrings(patron):
    print(re.findall(string, patron))
    #print(re.findall(r"aa([^\c]*?)gg", string))

obtener_substrings(patron)

#['tat'] 

def sin_c(string):
    return re.findall("aa([^c]*?)gg", string)
    
#2
class Auto:
    def _init_(self):
        self.cambio = 0
        self.rpm = 0
        self.consumo = 0.05 

    def arrancar(self):
         self.cambio += 1
         self.rpm += 500
   
    def subirCambio(self): 
        if self.cambio < 5:
            self.cambio += 1
    
    def bajarCambio(self):
        if self.cambio > 1:
            self.cambio -= 1
  
    def subirRPM(self, cantidad):
        if self.rpm + cantidad <= 5000:
            self.rpm += cantidad
        else:
            self.rpm = 5000
    
    def bajarRPM(self, cantidad):
        if self.rpm - cantidad >= 0:
            self.rpm -= cantidad

    def Velocidad(self):
        return ((self.rpm / 100) * (0.5 + (self.cambio / 2)))

    def consumoActualPorKm(self):
         if self.rpm > 3000:
             if self.cambio == 1:
                 return(self.consumo*((self.rpm - 2500) / 500)*3)
             elif self.cambio == 2:
                 return(self.consumo*((self.rpm - 2500) / 500)*2)
             elif self.cambio <= 5:
                 return(self.consumo*((self.rpm - 2500) / 500))
         elif self.cambio == 1:
             return(self.consumo*3)
         elif self.cambio == 2:
             return(self.consumo*2)
         else:
             return(self.consumo)
        #si los rpm son menores a 3000 y el auto en 3ra, 4ta o 5ta el consumo es el base

    def cambioActual(self):
        return (self.consumo)

    def rmpActual(self):
        return (self.rpm)

    auto1 = Auto()
    auto1.arrancar()
    auto1.subirRPM(3500)
    auto1.subirCambio()
    auto1.subirCambio()
    auto1.subirCambio()
    auto1.bajarCambio()
    auto1.Velocidad()
    auto1.consumoActualPorKm()
    #la velocidad debería es 80 y el consumo 0.15 litros/km.

#3
#a)
    #la corrida del script devuelve ZeroDivisionError, es decir, error por división por cero.
#b)
    #lo que agregue:
def obtener_media(lista):
    sumatoria = 0

    for valor in lista:

        sumatoria += valor
    longitud = len(lista)
    
    try:
        return sumatoria / longitud
    except ZeroDivisionError:
        print("no se puede obtener la media ya que la longitud es 0 y  no se puede dividir por dicho numero") #0 la lista esta vacia o algo del estilo

#c)
    #otra excepcion a considerar es TypeError, ya que se podria ingresar un valor a la lista que no sea de un tipo compatibe con la operacion, 
    #así como también un OverFlowError, si la división arroja un numero con muchos decimales

    #Se puede verificar que la lista es una lista, ya que si el parametro es de otro tipo (no iterable) el for no va a funcionar.

#4
import os
import glob

def unir_txt():
    os.mkdir("Resultado")

    lista_archivos = glob.glob("*.txt")
    with open("Resultado\\texto_completo.txt", 'a') as texto_completo:
        for archivo in lista_archivos:
            with open(archivo, 'r') as file:
                texto_completo.write(file.read())