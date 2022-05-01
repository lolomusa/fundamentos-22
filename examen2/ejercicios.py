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
#EJERCICIO 3

