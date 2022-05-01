import re
#1
#2
#3
#4
        import os
        import glob
        import re

        os.chdir(r"\Users\memal\OneDrive\Desktop\UCEMA\F_informatica\fundamentos-22\examen")
        os.mkdir("Resultado")

        lista_archivos = glob.glob("*.txt")

        with open("Resultado\texto_completo.txt", "a") as texto_completo:
            for archivo in lista_archivos:
                with open(archivo, "r") as file:
            texto_completo.write(file.read())
