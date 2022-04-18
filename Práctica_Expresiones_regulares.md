# **Expresiones Regulares**

##### **Ejercicio 1**
Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

        import re
                texto1= "A la grande le puse -Cuca-, 123456789"
                patron1="[A-Z0-9a-z]+"
                patron2="[2]"
                coincidencias=re.findall(patron1, texto1)
                print(coincidencias)
                print(len(coincidencias))

##### **Ejercicio 2**

Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

        import re 
        texto = "2. Tutor de la materia: Guillermo Benitez"
        re.search('\W', texto)

##### **Ejercicio 3**
Creá un programa que verifique las siguientes condiciones:
    
* si un string dado tiene una _h_ seguida de ninguna o más _e_.

* si un string dado tiene una _h_ seguida de una o más _e_.

* si un string dado tiene una _h_ seguida de una o más _e_.

* si un string dado tiene una _h_ seguida de dos o tres _e_.

##### **Ejercicio 4**
Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

        import re
        string = "Defíni la función aprobar_materias"
        patron = '\w' + '_' + '\w'
        re.search(patron, string) 

##### **Ejercicio 5**
Escribí un programa que diga si un string empieza con un número específico.

                import re
                string = input("ingrese una cadena de caracteres: ")
                patron = "^3"

                if re.match(patron, string) is not None:
                 print("el string comienza con el numero 3")
                else:
                 print("el string no emieza con el numero 3")

##### **Ejercicio 6**
Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

                import re
                 strings = ["hola", "te", "hoy"]
                 frase = "hola como te sentis hoy?"

                 for palabra in strings:
                     patron = palabra
                     if re.search(patron, frase) is not None:
                         print("la palabra esta en la frase")
                     else:
                         print("la palabra no esta en la frase")

##### **Ejercicio 7**
Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

                espacios y números.
                 import re
                 string = input("ingrese una frase: ")
                 patron = "[a-zA-Z0-9(\s)]"
                 coincidencias = []

                 for caracter in string:
                     coincidencias.append(re.findall(patron, caracter))
    
                 if len(coincidencias) == len(string):
                     print("todos los caracteres de la frase son o letras mayusculas, o letras minusculas, o numeros, o espacios")
                 else:
                     print("al menos un caracter no es una letra mayuscula o minuscula, numero o espacio")

##### **Ejercicio 8**
Escribí un programa que separe y devuelva los caracteres númericos de un string.

                import re
                 string = input("escriba algo: ")
                 patron = '\d'
                 lista = []

                 for caracter in string:
                     lista = re.findall(patron, string)

                 print(lista)

##### **Ejercicio 9**
Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: _"Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"_)

                 import re
                 string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
                 patron = "-(.*?)-"

                 print(re.findall(patron, string))

##### **Ejercicio 10**
Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres _@_ o _&_.

##### **Ejercicio 11**
Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: _["Práctica Python", "Práctica C++", "Práctica Fortran"]_).

                empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
                import re
                 lista_strings = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
                 patron = "(P\w*)\s(P\w*)"

                 for string in lista_strings:
                     coincidencia = re.search(patron, string)
                     if coincidencia is not None:
                         print(coincidencia.group())

##### **Ejercicio 12**
Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (**|**).

                barra vertical (|).
                 import re
                 string = "este documento se llama: expresiones_regulares.py"
                 patron = "[\s_:]"
                 print(re.sub(patron, "|", string))

##### **Ejercicio 13**
Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

##### **Ejercicio 14**
Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

        import re
                 string = "hola  mi nombre es    sol bertinat"
                 patron = "[\s]"
                 print(re.sub(patron, ";", string))

##### **Ejercicio 15**
Realizá un programa que validar si una cuenta de mail está escrita correctamente.