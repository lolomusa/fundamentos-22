#1
#a)
import re
texto = "xcabcb3sabc9"
patron = "abc"
print(re.search(patron, texto))
print(re.search(abc,xcabcb3sabc9))

<re.Match object; span=(3, 6), match='abc'>

import re
texto = "xcabcb3sabc9"
patron = "abc"
print(re.findall(patron, texto))
print(re.findall(abc,xcabcb3sabc9))

['abc', 'abc']

import re
texto = "hola amigos mios"
patron = "abc"
print(re.search(patron, texto))
print(re.search(abc,hola amigos mios))

None

import re
texto = "hola amigos mios"
patron = "abc"
print(re.findall(patron, texto))
print(re.findall(abc,hola amigos mios))

[]

#b)
import re
string = "aa([^c].*?)gg"  #aa literal | grupo de todo lo que no tenga c + cualquier caracter que se repita 0 o mas veces| gg literal
patron = "ttaatatggttaacatgg"

def obtener_substrings(patron):
    print(re.findall(string, patron))

obtener_substrings(patron)

['tat']

