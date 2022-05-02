#EJERCICIO 1
#a)
import re
texto = "xcabcb3sabc9"
patron = "abc"
print(re.search(patron, texto))
#print(re.search(abc,xcabcb3sabc9))

#resultado = <re.Match object; span=(3, 6), match='abc'>

import re
texto = "xcabcb3sabc9"
patron = "abc"
print(re.findall(patron, texto))
#print(re.findall(abc,xcabcb3sabc9))

#['abc', 'abc']

import re
texto = "hola amigos mios"
patron = "abc"
print(re.search(patron, texto))
#print(re.search(abc,hola amigos mios))

#resultado = None

import re
texto = "hola amigos mios"
patron = "abc"
print(re.findall(patron, texto))
#print(re.findall(abc, hola amigos mios))

#resultado = []

#b)
import re
string = "aa([^c].*?)gg"  
patron = "ttaatatggttaacatgg"

def obtener_substrings(patron):
    print(re.findall(string, patron))

obtener_substrings(patron)

#resultado = ['tat']

#EJERCICIO 2

class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5

    def potencia(self):
        print(self.potencia)

    def coraza(self):
        print(self.coraza)

    def encontrarPilaAtomica(self):
        self.potencia += 25
        if self.potencia >= 100:
            self.potencia -= (self.potencia - 100)

    def encontrarEscudo(self):
        self.coraza += 10
        if self.coraza >= 20:
            self.coraza -= (self.coraza - 20)     

    def recibirAtaque(self, puntos):
        resto = self.zoraza - puntos
        self.coraza -= puntos
        if self.coraza <= 0:
            self.coraza -= resto
        resto2 = self.potencia + resto
        self.potencia += resto
        if self.potencia <= 0:
          self.potencia -= resto2

    def fortalezaDefensiva(self):
        fortaleza = self.coraza + self.potencia
        print("la fortaleza defensiva es ", fortaleza, ", de la cual ", self.coraza, "son de coraza, y ", self.potencia)

    def necesitaFortalecerse(self):
        if self.coraza == 0 and self.potencia < 20:
          return True
        else:
            return False

    def fortalezaOfensiva(self):
        if self.potencia <= 20:
            print(0)
        else:
            print((self.potencia - 20) / 2)

enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
print(enterprise.potencia)
print(enterprise.coraza)

#la potencia de la Enterprise debe ser 66, y su coraza debe ser 10.

enterprise.fortalezaDefensiva() #toto 76
enterprise.necesitaFortalecerse() #False
enterprise.fortalezaOfensiva() #23

#EJERCICIO 3