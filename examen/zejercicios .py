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

obtener_substrings(patron)

#o 

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
         self.cambio += 1
    
    def bajarCambio(self):
         self.cambio -= 1
  
    def subirRPM(self, RPM):
         self.rpm += RPM
    
    def bajarRPM(self, RPM):
         self.rpm -= RPM

    def Velocidad(self):
         print((self.rpm / 100) * (0.5 + (self.cambio / 2)))

    def consumoActualPorKm(self):
         if self.rpm > 3000:
             if self.cambio == 1:
                 print(self.consumo*((self.rpm - 2500) / 500)*3)
             elif self.cambio == 2:
                 print(self.consumo*((self.rpm - 2500) / 500)*2)
             elif self.cambio <= 5:
                 print(self.consumo*((self.rpm - 2500) / 500))
         elif self.cambio == 1:
             print(self.consumo*3)
         elif self.cambio == 2:
             print(self.consumo*2)
         else:
             print(self.consumo)

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
#4
import os
import glob

os.chdir(r"\Users\memal\OneDrive\Desktop\UCEMA\F_informatica\fundamentos-22\examen")
os.mkdir("Resultado")

lista_archivos = glob.glob("*.txt")
with open("Resultado\\texto_completo.txt", 'a') as texto_completo:
    for archivo in lista_archivos:
        with open(archivo, 'r') as file:
            texto_completo.write(file.read())