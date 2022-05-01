#1
b)
string = "aa([^c].*?)gg"  #aa literal | grupo de todo lo que no tenga c + cualquier caracter que se repita 0 o mas veces| gg literal
patron = "ttaatatggttaacatgg"

def obtener_substrings(patron):
    print(re.findall(string, patron))

obtener_substrings(patron)